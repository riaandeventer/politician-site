from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('authorize', views.authorize_user, name='authorize'),
  ]