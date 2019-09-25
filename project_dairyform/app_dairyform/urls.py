from django.urls import path
from .import views
from dairyformapp import views
urlpatterns = [
    path('', views.FarmerFormView.as_view(), name='FarmerFormView'),
]
