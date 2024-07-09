from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def email_confirmation(request):
    return render(request, 'user_accounts_app/email_confirmation.html')

@login_required
def profile_view(request):
    return render(request, 'user_accounts_app/profile.html')
