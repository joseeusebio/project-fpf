
from rest_framework import serializers
from games import models
from django.core.exceptions import ObjectDoesNotExist

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

    def create(self, validated_data):
        category_name = validated_data['name'].lower()
        try:
            models.Category.objects.get(name=category_name)
        except ObjectDoesNotExist:
            pass
        else:
            raise serializers.ValidationError(f'This category {category_name} already exists')

        return super().create(validated_data)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

    def create(self, validated_data):
        company_name = validated_data['name'].lower()
        try:
            models.Company.objects.get(name=company_name)
        except ObjectDoesNotExist:
            pass
        else:
            raise serializers.ValidationError(f'This company {company_name} already exists')

        return super().create(validated_data)

class GameSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all(), source='category.id')
    # company = serializers.PrimaryKeyRelatedField(queryset=models.Company.objects.all(), source='company.id')
    class Meta:
        model = models.Game
        fields = (
            'id', 'title', 'slug', 'description', 'release_date', 'category', 'company', 'price',
            'quantity', 'is_activate', 'picture'
        )