from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
# from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
import re

try:
    from django.contrib.auth import get_user_model

    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User


class FirstnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        first_name = data['firstname']

        if not str(first_name).isalnum():
            return JsonResponse({'firstname_error': 'First name should only contain alphanumeric characters'},
                                status=400)
        return JsonResponse({'firstname_valid': True})


class LastnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        last_name = data['lastname']

        if not str(last_name).isalnum():
            return JsonResponse({'lastname_error': 'Last name should only contain alphanumeric characters'},
                                status=400)
        return JsonResponse({'lastname_valid': True})


class SchoolValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        school = data['school']

        if not str(school).isalnum():
            return JsonResponse({'school_error': 'School/Facility name should only contain alphanumeric characters'},
                                status=400)
        return JsonResponse({'school_valid': True})


class PostalValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        post_code = data['postal']
        # Canadian postal codes can't contain the letters D, F, I, O, Q, or U, and cannot start with W or Z，
        # We allow an optional space in the middle
        if not re.match(r'[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]',
                        post_code):
            return JsonResponse({'postal_error': 'Invalid Canadian postal code'},
                                status=400)
        return JsonResponse({'postal_valid': True})


class BirthYearValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        birth_year = data['birth']

        if not re.match(r'\b(19[3456789][0-9]|200[0-3]|2003)\b', birth_year):
            return JsonResponse({'birth_error': 'Birth year should between 1930 and 2003'}, status=400)
        return JsonResponse({'birth_valid': True})


class YearValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        year = data['year']

        if not re.match(r'\b([1-9]|[1-7][0-9])\b', year):
            return JsonResponse({'year_error': 'Years of experience should between 1 and 79'}, status=400)
        return JsonResponse({'year_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username in use, please choose another one'}, status=409)
        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email in use, please choose another one'}, status=409)
        return JsonResponse({'email_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/registernew.html')

    def post(self, request):
        # messages.success(request, "Success whatsapp success")
        # messages.warning(request, "Success whatsapp warning")
        # messages.info(request, "Success whatsapp info")
        # messages.error(request, "Success whatsapp error")
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password shall be more than 6 characters')
                    return render(request, 'authentication/registernew.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                email_subject = "Activate your account"
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
                activate_url = 'http://' + domain + link
                email_body = "Hi " + user.username + ',\nPlease use this link to verify your account\n' + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email]
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account successfully created')
                return render(request, 'authentication/registernew.html')

        return render(request, 'authentication/registernew.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('loginnew' + '?message=' + 'User already activated')

            if user.is_active:
                return redirect('loginnew')

            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('loginnew')
        except Exception as ex:
            pass

        return redirect('loginnew')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/loginnew.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' + user.username + ' You are now logged in')
                    return redirect('expenses')
                messages.error(request, 'Account is not active, please check your email ')
                return render(request, 'authentication/loginnew.html')
            messages.error(request, 'Invalid credentials, try again')
            return render(request, 'authentication/loginnew.html')
        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/loginnew.html')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('loginnew')


class RequestPasswordResetEmail(View):
    def get(self, request):
        return render(request, 'authentication/reset-password.html')

    def post(self, request):
        email = request.POST['email']
        context = {
            'values': request.POST
        }

        if not validate_email(email):
            message.error(request, 'Please supply a valid email')
            return render(request, 'authentication/reset-password.html', context)

        user = User.objects.filter(email=email)

        if user.exists():
            email_contents = {
                'user': user[0],
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])
            }
            email_subject = "Password reset instructions"
            domain = get_current_site(request).domain
            link = reverse('reset-user-password',
                           kwargs={'uidb64': email_contents['uid'], 'token': email_contents['token']})
            reset_url = 'http://' + domain + link
            email_body = "Hi there" + ',\nPlease use this link to reset your password\n' + reset_url
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email]
            )
            email.send(fail_silently=False)

        messages.success(request, 'We have sent you an email to reset your password')
        return render(request, 'authentication/reset-password.html')


class CompletePasswordReset(View):
    def get(self, request, uidb64, token):

        context = {
            'uidb64': uidb64,
            'token': token
        }
        return render(request, 'authentication/set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }

        password = request.POST['password']
        passwordnew = request.POST['passwordnew']

        if password != passwordnew:
            messages.error(request, 'Password do not match')
            return render(request, 'authentication/set-new-password.html', context)

        if len(password) < 6:
            messages.error(request, 'Password should be more than 6 characters')
            return render(request, 'authentication/set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            # user.password = password
            user.save()

            messages.success(request, 'Password reset successful, you can login with your new password')
            return redirect('loginnew')
        except Exception as identifier:
            import pdb
            pdb.set_trace()
            messages.info(request, 'Something went wrong, try again')
            return render(request, 'authentication/set-new-password.html', context)
