from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

from contact.models import Contact


def contact_us(request):

    if request.method == 'GET':
        return render(request, 'contact/contact-us.html')

    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        comments = request.POST['comments']

        if not email:
            messages.error(request, 'Email is required')
            return render(request, 'contact/contact-us.html')

        if not subject:
            messages.error(request, 'Subject is required')
            return render(request, 'contact/contact-us.html')

        if not comments:
            messages.error(request, 'Comments is required')
            return render(request, 'contact/contact-us.html')

        Contact.objects.create(email=email, subject=subject, message=comments)

        email_body = "Hi Admin," + '\nUser sent you a message from email: ' + email + '\n' + comments
        email = EmailMessage(
            subject,
            email_body,
            'noreply@outofourpockets.ca',
            [email]
        )
        email.send(fail_silently=False)

        messages.success(request, 'Comments submitted successfully')
        return redirect('contact-us')

    return render(request, 'contact/contact-us.html')