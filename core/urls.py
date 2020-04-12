from django.urls import path

from .views import sign_up, sign_in, sign_out

urlpatterns = [
    path('signup', sign_up, name='sign_up'),
    path('signin', sign_in, name='sign_in'),
    path('signout', sign_out, name='sign_out'),
]
