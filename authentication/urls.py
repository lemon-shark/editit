from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView, LoginView, \
    LogoutView, RequestPasswordResetEmail, CompletePasswordReset
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registernew', RegistrationView.as_view(), name='registernew'),
    path('loginnew', LoginView.as_view(), name='loginnew'),
    path('logoutnew', LogoutView.as_view(), name='logoutnew'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>', CompletePasswordReset.as_view(), name='reset-user-password'),
    path('request-reset-link', RequestPasswordResetEmail.as_view(), name='request-password')
]