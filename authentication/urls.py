from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView, LoginView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registernew', RegistrationView.as_view(), name='registernew'),
    path('loginnew', LoginView.as_view(), name='loginnew'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
]