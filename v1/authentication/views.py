from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import CustomUser, EmailVerification, GoogleOAuth2Token
from .serializers import UserSerializer, LoginSerializer, ResetPasswordSerializer, VerifyEmailSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests
import datetime
import json
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class SignupView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            user_data = UserSerializer(user).data

            # Create EmailVerification instance
            expiration_time = timezone.now() + timezone.timedelta(hours=24)  # Set expiration to 24 hours from now
            email_verification = EmailVerification.objects.create(user=user, expires_at=expiration_time)

            # Send verification email
            verification_url = f"{settings.FRONTEND_URL}/verify-email?token={email_verification.token}&email={user.email}"
            send_mail(
                'Verify your email',
                f'Please click the following link to verify your email: {verification_url}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return Response({
                'token': token.key,
                'user': user_data,
                'message': 'Verification email sent. Please check your inbox.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                user_data = UserSerializer(user).data
                return Response({
                    'token': token.key,
                    'user': user_data
                }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.filter(email=serializer.validated_data['email']).first()
            if user:
                # Generate and send reset token (implement this part)
                return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class VerifyEmailView(APIView):
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.filter(email=serializer.validated_data['email']).first()
            if user:
                # Verify email logic (implement this part)
                return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid verification data'}, status=status.HTTP_400_BAD_REQUEST)

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class GoogleLoginView(APIView):
    def get(self, request):
        google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth"
        params = {
            "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
            "redirect_uri": settings.GOOGLE_OAUTH2_REDIRECT_URI,
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent",
        }
        url = f"{google_auth_url}?{requests.compat.urlencode(params)}"
        return redirect(url)

@method_decorator(csrf_exempt, name='dispatch')
class GoogleCallbackView(APIView):
    def get(self, request):
        code = request.GET.get("code")
        if not code:
            return Response({"error": "No code provided"}, status=status.HTTP_400_BAD_REQUEST)

        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
            "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_OAUTH2_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        token_response = requests.post(token_url, data=token_data)
        token_json = token_response.json()

        if "error" in token_json:
            return Response({"error": token_json["error"]}, status=status.HTTP_400_BAD_REQUEST)

        access_token = token_json["access_token"]
        refresh_token = token_json.get("refresh_token")
        expires_in = token_json["expires_in"]
        expires_at = timezone.now() + datetime.timedelta(seconds=expires_in)

        user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        user_info_response = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"})
        user_info = user_info_response.json()

        email = user_info["email"]
        user, created = CustomUser.objects.get_or_create(email=email)
        if created:
            user.username = user_info["email"]
            user.name = user_info["name"]
            user.save()

        GoogleOAuth2Token.objects.update_or_create(
            user=user,
            defaults={
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_at": expires_at,
            },
        )

        token, _ = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data

        frontend_url = settings.FRONTEND_URL  # Assuming you have this in your settings
        redirect_url = f"{frontend_url}/oauth/login"
        
        params = {
            "token": token.key,
            "user": json.dumps(user_data)  # Convert user_data to JSON string
        }
        
        full_redirect_url = f"{redirect_url}?{urlencode(params)}"
        return redirect(full_redirect_url, permanent=False)


