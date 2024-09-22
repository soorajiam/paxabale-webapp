from django.urls import path
from .views import SignupView, LoginView, ResetPasswordView, VerifyEmailView, GoogleLoginView, GoogleCallbackView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/google/', GoogleLoginView.as_view(), name='google_login'),
    path('login/google/callback/', GoogleCallbackView.as_view(), name='google_callback'),
]