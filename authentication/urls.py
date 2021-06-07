from .views import RegistrationView
from django.urls import path

urlpatterns = [
    path('registernew', RegistrationView.as_view(), name='registernew')
]