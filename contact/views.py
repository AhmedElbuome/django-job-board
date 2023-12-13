from django.shortcuts import render, redirect
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from .models import Info  # Import your Info model

def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST.get('subject', '')  # Use get() to avoid potential KeyError
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Validate that required fields are not empty
        if not subject or not email or not message:
            # Handle validation error, e.g., return an error message to the user
            return render(request, 'contact/contact.html', {'myinfo': myinfo, 'error_message': 'All fields are required.'})

        try:
            # Send email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  # Use a valid sender email
                [email],
                fail_silently=False,
            )

            # Optionally, you can redirect the user to a success page
            return redirect('contact:success_page')  # Replace 'success_page' with the name of your success page

        except Exception as e:
            # Handle the exception, e.g., return an error message to the user
            return render(request, 'contact/contact.html', {'myinfo': myinfo, 'error_message': str(e)})

    context = {'myinfo': myinfo}
    return render(request, 'contact/contact.html', context)

def success_page(request):
    return render(request, 'contact/success.html')  # Update the path based on your project structure
