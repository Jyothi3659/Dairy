from django.contrib import admin
from django.urls import path,include
from app_dairyform import views
from django.urls import path, include

urlpatterns = [
    path('',include('app_dairyform.urls')),
    path('app_dairyform/', include('app_dairyform.urls')),
    path('admin/', admin.site.urls),
    path('about/',include('app_dairyform.urls')),
    path('email us/',include('app_dairyform.urls')),
    path('app_dairyform/', include('app_dairyform.urls')),
]







