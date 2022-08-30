from rest_framework import viewsets, permissions
from games import models
from games.api import serializers
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
        
class GameViewSet(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','category__name','company__name']