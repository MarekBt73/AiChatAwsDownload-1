from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import CustomUserChangeForm
from allauth.account.views import SignupView
from django.db import transaction
import logging


logger = logging.getLogger(__name__)




def email_confirmation(request):
    return render(request, '/account/email_confirm.html')

@login_required
def profile_view(request):
    user = request.user
    print(f"User subjects: {user.subjects}")
    return render(request, 'user_accounts_app/profile.html', {'user': user})


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'user_accounts_app/edit_profile.html', {'form': form})


class CustomSignupView(SignupView):

    def form_valid(self, form):
        try:
            with transaction.atomic():
                response = super().form_valid(form)
                user = form.save(self.request)
                logger.info(f'User created: {user}')
                return response
        except Exception as e:
            logger.error(f'Error during signup: {e}')
            form.add_error(None, str(e))
            return self.form_invalid(form)