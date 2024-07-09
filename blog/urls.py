from django.urls import path
from .views import home, contact
from django.conf.urls import handler404
from .views import home, contact

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]


