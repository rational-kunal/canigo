from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('broker/', include('ticketbroker.urls')),
    path('review/', include('reviewer.urls')),
    path('', lambda r: redirect('staff_home') if r.user.is_staff else redirect('user_home')),
]
