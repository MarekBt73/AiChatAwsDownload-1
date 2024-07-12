from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_material, name='add_material'),
    path('edit/<int:pk>/', views.edit_material, name='edit_material'),
    path('', views.material_list, name='material_list'),
]
