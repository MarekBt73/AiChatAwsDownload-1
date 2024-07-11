from django.urls import path
from .views import home, custom_page_not_found_view,contact_view, contact_success

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]



    
handler404 = 'blog.views.custom_page_not_found_view'


