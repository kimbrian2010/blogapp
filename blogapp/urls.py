from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='blog-home'),
    path('userpost/', views.user_profile_post, name='user-post'),
    path('about/', views.about, name='about'),
]