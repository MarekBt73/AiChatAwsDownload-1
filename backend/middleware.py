# your_app/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class CustomLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Sprawdzenie, czy użytkownik jest zalogowany i nie został jeszcze przekierowany
        if request.user.is_authenticated and not request.session.get('has_logged_in'):
            request.session['has_logged_in'] = True
            # Przekierowanie superużytkownika do strony admina
            if request.user.is_superuser:
                return redirect(reverse('admin:index'))
            # Przekierowanie zwykłego użytkownika do strony profilu
            else:
                return redirect(reverse('profile'))

        response = self.get_response(request)
        return response
