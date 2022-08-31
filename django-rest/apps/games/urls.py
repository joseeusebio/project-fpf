from django.urls import path, include
from rest_framework import routers
from .api import viewsets as gameviewsets

router = routers.DefaultRouter()

router.register(r'games',gameviewsets.GameViewSet, basename="Game")
router.register(r'categories',gameviewsets.CategoryViewSet, basename="Category")
router.register(r'companies',gameviewsets.CompanyViewSet, basename="Company")


urlpatterns = [
    path('products/',include(router.urls)),
]
