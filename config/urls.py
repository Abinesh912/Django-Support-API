from django.contrib import admin
from django.urls import path, include
from tickets.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tickets/', include('tickets.urls')),
    path('health/', health_check, name='health-check'),
]