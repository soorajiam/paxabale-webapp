import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import StripeCustomer, Plan, Subscription, Payment
from django.utils import timezone

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_checkout_session(request):
    try:
        # plan = Plan.objects.get(id=request.data['priceId'])
        # stripe_customer = StripeCustomer.get_or_create(request.user)
        checkout_session = stripe.checkout.Session.create(
            # customer=7,
            payment_method_types=['card'],
            line_items=[{
                'price': request.data['priceId'],
                'quantity': 1,
            }],
            mode='subscription',
            success_url=request.build_absolute_uri('/payment-success/'),
            cancel_url=request.build_absolute_uri('/payment-cancelled/'),
        )
        return Response({'sessionId': checkout_session.id})
    except Plan.DoesNotExist:
        return Response({'error': 'Plan not found'}, status=404)
    except stripe.error.StripeError as e:
        return Response({'error': str(e)}, status=400)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_checkout_session(session)
    elif event['type'] == 'invoice.paid':
        invoice = event['data']['object']
        handle_invoice_paid(invoice)
    elif event['type'] == 'invoice.payment_failed':
        invoice = event['data']['object']
        handle_payment_failed(invoice)

    return JsonResponse({'status': 'success'})

def handle_checkout_session(session):
    customer_id = session['customer']
    subscription_id = session['subscription']
    
    stripe_customer = StripeCustomer.objects.get(stripe_customer_id=customer_id)
    stripe_subscription = stripe.Subscription.retrieve(subscription_id)
    
    plan = Plan.objects.get(stripe_price_id=stripe_subscription['items']['data'][0]['price']['id'])
    
    Subscription.objects.create(
        user=stripe_customer.user,
        stripe_subscription_id=subscription_id,
        plan=plan,
        status=stripe_subscription.status,
        current_period_end=timezone.datetime.fromtimestamp(stripe_subscription.current_period_end)
    )

def handle_invoice_paid(invoice):
    subscription_id = invoice['subscription']
    subscription = Subscription.objects.get(stripe_subscription_id=subscription_id)
    subscription.status = 'active'
    subscription.current_period_end = timezone.datetime.fromtimestamp(invoice['lines']['data'][0]['period']['end'])
    subscription.save()

def handle_payment_failed(invoice):
    subscription_id = invoice['subscription']
    subscription = Subscription.objects.get(stripe_subscription_id=subscription_id)
    subscription.status = 'past_due'
    subscription.save()

@api_view(['GET'])
def list_plans(request):
    plans = Plan.objects.all()
    data = [{
        'id': plan.id,
        'name': plan.name,
        'price': str(plan.price),
        'interval': plan.interval,
        'description': plan.description
    } for plan in plans]
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer_subscription(request):
    try:
        subscription = Subscription.objects.get(user=request.user, status='active')
        return Response({
            'plan': subscription.plan.name,
            'status': subscription.status,
            'current_period_end': subscription.current_period_end,
        })
    except Subscription.DoesNotExist:
        return Response({'error': 'No active subscription found'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_subscription(request):
    try:
        subscription = Subscription.objects.get(user=request.user, status='active')
        stripe_subscription = stripe.Subscription.modify(
            subscription.stripe_subscription_id,
            cancel_at_period_end=True
        )
        subscription.status = 'canceling'
        subscription.save()
        return Response({'status': 'Subscription will be canceled at the end of the billing period'})
    except Subscription.DoesNotExist:
        return Response({'error': 'No active subscription found'}, status=404)
    except stripe.error.StripeError as e:
        return Response({'error': str(e)}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-timestamp')
    data = [{
        'amount': str(payment.amount),
        'timestamp': payment.timestamp,
        'payment_intent_id': payment.stripe_payment_intent_id
    } for payment in payments]
    return Response(data)

@api_view(['GET'])
def list_subscriptions(request):
    plans = Plan.objects.all()
    data = [{
        'id': plan.id,
        'name': plan.name,
        'price': str(plan.price),
        'interval': plan.interval,
        'description': plan.description
    } for plan in plans]
    return Response(data)

# list all the plans available in the product in stripe
@api_view(['GET'])
def list_plans(request):
    plans = stripe.Plan.list()
    plan_data = []
    # get the product name from the plan
    for plan in plans:
        product = stripe.Product.retrieve(plan['product'])
        product['plan_details'] = plan
        plan_data.append(
            product
        )
    return Response(plan_data)