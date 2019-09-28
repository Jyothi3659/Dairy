from django.urls import path
from .import views
#from app_dairyform import views
urlpatterns = [
    path('', views.FarmerFormView.as_view(), name='FarmerFormView'),
    path('app_dairyform/', views.FarmerFormView.as_view(), name='FarmerFormView'),
    path('save', views.FarmerFormView.as_view(), name='FarmerFormView'),
]
