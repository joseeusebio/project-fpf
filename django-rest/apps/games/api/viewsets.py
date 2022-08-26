from rest_framework import viewsets, permissions, generics
from games import models
from games.api import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GameSerializer
    queryset = models.Game.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListGamesByCategoryViewSet(generics.ListAPIView):
    """Listando os games por categoria"""
    queryset = models.Game.objects.all()
    serializer_class = serializers.ListGamesByCategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__id']
    
    # def get_queryset(self):
    #     query_set = models.Game.objects.filter(category=self.kwargs['pk'])
    #     return query_set
        