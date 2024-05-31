from django.contrib import admin
from django.urls import path, include
from cars import views as car_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', car_views.home, name='home'),  # Ensure home page routes correctly
    path('', include('cars.urls', namespace='cars')),
    path('accounts/', include('django.contrib.auth.urls')),
]
