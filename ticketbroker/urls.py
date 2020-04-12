from django.urls import path

from .views import create_ticket, home

urlpatterns = [
    path('create', create_ticket, name='create_ticket'),
    path('', home, name='user_home'),
]
