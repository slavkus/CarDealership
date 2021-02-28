"""car_dealership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_cars import views as app_views

urlpatterns = [
    path('', app_views.index, name='index'),
    path('add_car', app_views.add_car, name='add_car'),
    path('update_specs', app_views.update_specs, name='update_specs'),
    path('admin/', admin.site.urls),
    path('add_specs/<int:car_id>', app_views.add_specs, name='add_specs'),
]
