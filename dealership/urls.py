from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user_authentication import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('user_authentication/', include('user_authentication.urls')),
    path('', auth_views.home, name='home'),
    path('home/', auth_views.home, name='home'),
]
