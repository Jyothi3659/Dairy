from django.urls import path
from . import views
from app_dairyform import views
urlpatterns = [
    path('',views.home,name='home'),
    path('app_dairyform/', views.FarmerFormView.as_view(), name='FarmerFormView'),
    path("app_dairyform/home_name/",views.about),
    path('app_dairyform/123/',views.about),
    path('123/',views.about),
    path('123/home_name/',views.home1),
    path('543/',views.email),
    path('app_dairyform/app_dairyform/', views.FarmerFormView.as_view(), name='FarmerFormView'),
    path('app_dairyform/app_dairyform/app_dairyform', views.FarmerFormView.as_view(), name='FarmerFormView'),
]
