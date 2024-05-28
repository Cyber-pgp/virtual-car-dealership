from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='car_list'),
    path('list/', views.CarListView.as_view(), name='car_listings'),
    path('<int:id>/', views.car_detail, name='car_detail'),
    path('add/', views.CarCreateView.as_view(), name='car_add'),
    path('<int:pk>/edit/', views.CarUpdateView.as_view(), name='car_edit'),
    path('<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),


    # This is all path details of home,list,details,search
    path('', views.home, name='home'),
    path('list/', views.listings, name='listings'),
    path('cars/<int:car_id>/', views.car_details, name='car_details'),
    path('search/', views.search, name='search'),



]
