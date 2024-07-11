from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponse
from .forms import ContactForm
from .models import ContactMessage  # Import the model


def home(request):
    return render(request, 'blog/home.html')


def custom_page_not_found_view(request, exception):
    return render(request, 'blog/404.html', {}, status=404)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Create the email message
            email_message = f"Imię: {name}\nEmail: {email}\n\nWiadomość:\n{message}"
            
            try:
                # Save the message to the database
                contact_message = ContactMessage(name=name, email=email, message=message)
                contact_message.save()
                
                # Send the email
                send_mail(
                    subject=f'Wiadomość od {name} ({email})',
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['mayster.app@mbecht.pl'],
                    fail_silently=False,
                )
                return redirect('contact_success')
            except Exception as e:
                return HttpResponse(f'Nie udało się wysłać wiadomości: {str(e)}')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'blog/contact_success.html')




def custom_page_not_found_view(request, exception):
    return render(request, 'blog/404.html', {}, status=404)