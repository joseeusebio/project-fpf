"""fromgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.games.api import viewsets as gameviewsets

route = routers.DefaultRouter()

route.register(r'games',gameviewsets.GameViewSet, basename="Game")
route.register(r'categories',gameviewsets.CategoryViewSet, basename="Category")
route.register(r'companies',gameviewsets.CompanyViewSet, basename="Company")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
    path('list_category_games/<int:pk>', gameviewsets.ListGamesByCategoryViewSet.as_view(), name='categoy__id')
]
