from django.shortcuts import render, redirect
from django.contrib import messages

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

        if not comments:
            messages.error(request, 'Comments is required')
            return render(request, 'contact/contact-us.html')

        Contact.objects.create(email=email, subject=subject, message=comments)

        messages.success(request, 'Comments submitted successfully')
        return redirect('contact-us')

    return render(request, 'contact/contact-us.html')