from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import CustomUserChangeForm
from allauth.account.views import SignupView
from django.db import transaction
import logging
from apiAi.models import Chat
from .models import StudentActivity, StudentProgress

logger = logging.getLogger(__name__)


def email_confirmation(request):
    return render(request, "/account/email_confirm.html")


@login_required
def profile_view(request):
    user = request.user
    activities = StudentActivity.objects.filter(user=user).order_by("-timestamp")
    progress = StudentProgress.objects.filter(user=user)
    chats = Chat.objects.filter(user=user).order_by("-created_at")
    return render(
        request,
        "user_accounts_app/profile.html",
        {"user": user, "activities": activities, "progress": progress, "chats": chats},
    )


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "user_accounts_app/edit_profile.html", {"form": form})


@login_required
def chat_detail_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, user=request.user)
    return render(request, "user_accounts_app/chat_detail.html", {"chat": chat})


class CustomSignupView(SignupView):

    def form_valid(self, form):
        try:
            with transaction.atomic():
                response = super().form_valid(form)
                user = form.save(self.request)
                logger.info(f"User created: {user}")
                return response
        except Exception as e:
            logger.error(f"Error during signup: {e}")
            form.add_error(None, str(e))
            return self.form_invalid(form)
