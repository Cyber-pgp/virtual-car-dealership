from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars import views as car_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', car_views.home, name='home'),
    path('cars/', include('cars.urls', namespace='cars')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
