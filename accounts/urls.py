from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.account, name='account'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
]
