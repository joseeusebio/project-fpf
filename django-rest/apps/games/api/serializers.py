
from rest_framework import serializers
from games import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    company = CompanySerializer(many=True)
    class Meta:
        model = models.Game
        fields = (
            'id', 'title', 'slug', 'description', 'release_date', 'category', 'company', 'price',
            'quantity', 'is_activate', 'picture'
        )