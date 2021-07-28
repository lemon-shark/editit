from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView, LoginView, \
    LogoutView, RequestPasswordResetEmail, CompletePasswordReset, FirstnameValidationView, LastnameValidationView, \
    SchoolValidationView, PostalValidationView, BirthYearValidationView, YearValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registernew', RegistrationView.as_view(), name='registernew'),
    path('loginnew', LoginView.as_view(), name='loginnew'),
    path('logoutnew', LogoutView.as_view(), name='logoutnew'),
    path('validate-firstname', csrf_exempt(FirstnameValidationView.as_view()), name='validate-firstname'),
    path('validate-lastname', csrf_exempt(LastnameValidationView.as_view()), name='validate-lastname'),
    path('validate-school', csrf_exempt(SchoolValidationView.as_view()), name='validate-school'),
    path('validate-postal', csrf_exempt(PostalValidationView.as_view()), name='validate-postal'),
    path('validate-birth', csrf_exempt(BirthYearValidationView.as_view()), name='validate-birth'),
    path('validate-year', csrf_exempt(YearValidationView.as_view()), name='validate-year'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>', CompletePasswordReset.as_view(), name='reset-user-password'),
    path('request-reset-link', RequestPasswordResetEmail.as_view(), name='request-password')
]