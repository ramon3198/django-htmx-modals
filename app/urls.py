from django import urls
from django.contrib import admin
from django.urls import path, include
from app import urls
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/',views.agregarVlan, name='add')
]
