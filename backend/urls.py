from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user_accounts_app.urls')),
    path('', include('blog.urls')),
    path('materials/', include('content_management.urls')),
    path('apiAi/', include('apiAi.urls')),  # Dodana ścieżka do nowej aplikacji
]
handler404 = 'blog.views.custom_page_not_found_view'

