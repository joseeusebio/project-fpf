
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
    # category = CategorySerializer(read_only=False)
    # company = CompanySerializer(read_only=False)
    class Meta:
        model = models.Game
        fields = '__all__'

# class ListGamesByCategorySerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#     company = CompanySerializer(read_only=True)
#     class Meta:
#         model = models.Game
#         fields = ['id','title','description','release_date','price','category','company']