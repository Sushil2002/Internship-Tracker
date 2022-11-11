from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/' , views.create_post, name='new_post'),
    path('register/' , views.user_register, name ='register'),
    path('login/' , views.user_login, name ='login'),
    path('logout/' , views.user_logout, name ='logout'),
    path('allposts/' , views.show_all_posts, name ='all_posts'),
    path('profile/<int:pk>' , views.my_profile, name ='profile'),
    path('post/<int:pk>' , views.post_detail, name ='post-detail'),
    path('post/update/<int:pk>' , views.update_post, name ='update-post'),
    path('post/delete/<int:pk>' , views.delete_post, name ='delete-post'),
    path('about/', views.about, name='about'),
]