import stripe
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import StripeCustomer, RazorpayCustomer, Plan, Subscription, Payment
from django.utils import timezone

stripe.api_key = settings.STRIPE_SECRET_KEY
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@api_view(['POST'])
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_razorpay_order(request):
    try:
        amount = request.data.get('amount')
        currency = request.data.get('currency', 'INR')
        
        order = razorpay_client.order.create({
            'amount': int(float(amount) * 100),  # Amount in paise
            'currency': currency,
            'payment_capture': '0'  # Manual capture for added security
        })
        
        return Response({
            'order_id': order['id'],
            'amount': amount,
            'currency': currency,
            'key': settings.RAZORPAY_KEY_ID
        })
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_razorpay_payment(request):
    try:
        payment_id = request.data.get('razorpay_payment_id')
        order_id = request.data.get('razorpay_order_id')
        signature = request.data.get('razorpay_signature')
        
        params_dict = {
            'razorpay_payment_id': payment_id,
            'razorpay_order_id': order_id,
            'razorpay_signature': signature
        }
        razorpay_client.utility.verify_payment_signature(params_dict)
        
        razorpay_client.payment.capture(payment_id, razorpay_client.order.fetch(order_id)['amount'])
        
        Payment.objects.create(
            user=request.user,
            amount=razorpay_client.order.fetch(order_id)['amount'] / 100,
            razorpay_payment_id=payment_id,
            razorpay_order_id=order_id,
            status='success'
        )
        
        return Response({'status': 'Payment successful'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_razorpay_subscription(request):
    try:
        plan_id = request.data.get('plan_id')
        plan = Plan.objects.get(id=plan_id)
        
        subscription = razorpay_client.subscription.create({
            'plan_id': plan.razorpay_plan_id,
            'customer_notify': 1,
            'total_count': 12,  # For example, 12 months subscription
        })
        
        return Response({
            'subscription_id': subscription['id'],
            'short_url': subscription['short_url']
        })
    except Plan.DoesNotExist:
        return Response({'error': 'Plan not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_razorpay_subscription(request):
    try:
        subscription_id = request.data.get('razorpay_subscription_id')
        payment_id = request.data.get('razorpay_payment_id')
        signature = request.data.get('razorpay_signature')
        
        params_dict = {
            'razorpay_subscription_id': subscription_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        razorpay_client.utility.verify_subscription_payment_signature(params_dict)
        
        subscription_details = razorpay_client.subscription.fetch(subscription_id)
        Subscription.objects.create(
            user=request.user,
            razorpay_subscription_id=subscription_id,
            plan=Plan.objects.get(razorpay_plan_id=subscription_details['plan_id']),
            status='active',
            current_period_end=timezone.datetime.fromtimestamp(subscription_details['current_end'])
        )
        
        return Response({'status': 'Subscription successful'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@csrf_exempt
def razorpay_webhook(request):
    webhook_secret = settings.RAZORPAY_WEBHOOK_SECRET
    received_signature = request.headers.get('X-Razorpay-Signature')
    
    if razorpay_client.utility.verify_webhook_signature(request.body.decode(), received_signature, webhook_secret):
        payload = json.loads(request.body)
        event = payload['event']
        
        if event == 'subscription.charged':
            handle_subscription_charged(payload['payload']['subscription']['entity'])
        elif event == 'subscription.cancelled':
            handle_subscription_cancelled(payload['payload']['subscription']['entity'])
        
        return JsonResponse({'status': 'Webhook processed'})
    else:
        return JsonResponse({'status': 'Invalid signature'}, status=400)

def handle_subscription_charged(subscription_data):
    subscription = Subscription.objects.get(razorpay_subscription_id=subscription_data['id'])
    subscription.current_period_end = timezone.datetime.fromtimestamp(subscription_data['current_end'])
    subscription.save()
    
    Payment.objects.create(
        user=subscription.user,
        amount=subscription_data['amount'] / 100,
        razorpay_payment_id=subscription_data['payment_id'],
        status='success'
    )

def handle_subscription_cancelled(subscription_data):
    subscription = Subscription.objects.get(razorpay_subscription_id=subscription_data['id'])
    subscription.status = 'cancelled'
    subscription.save()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_razorpay_subscriptions(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    data = [{
        'id': sub.razorpay_subscription_id,
        'status': sub.status,
        'plan_name': sub.plan.name,
        'current_period_end': sub.current_period_end
    } for sub in subscriptions]
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_razorpay_subscription(request):
    try:
        subscription_id = request.data.get('subscription_id')
        subscription = Subscription.objects.get(razorpay_subscription_id=subscription_id, user=request.user)
        
        razorpay_client.subscription.cancel(subscription_id)
        
        subscription.status = 'cancelled'
        subscription.save()
        
        return Response({'status': 'Subscription cancelled successfully'})
    except Subscription.DoesNotExist:
        return Response({'error': 'Subscription not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)