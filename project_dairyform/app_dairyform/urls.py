from django.urls import path
from .import views
from app_dairyform import views
#from app_dairyform import views
urlpatterns = [
    path('app_dairyform/', views.FarmerFormView.as_view(), name='FarmerFormView'),
    path('',views.home,name='home'),
    path('123/',views.about),
    path('543/',views.email),
    path('',views.response),
    # path('', views.FarmerFormView.as_view(), name='FarmerFormView'),
]
