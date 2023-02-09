from django.urls import path
from . import views

app_name = 'personal'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('programs', views.programs, name='programs'),
    path('vips', views.vips, name='vips'),
    path('contact', views.contact, name='contact'),
]