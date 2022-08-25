from rest_framework import viewsets
from games import models
from games.api import serializers

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GameSerializer
    queryset = models.Game.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()