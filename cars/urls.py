from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings, name='listings'),  # Changed from 'list' to 'listings'
    path('cars<int:car_id>/', views.car_details, name='car_details'),  # Removed redundant 'cars' prefix
    path('search/', views.search, name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


