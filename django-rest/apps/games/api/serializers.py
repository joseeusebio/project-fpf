from dataclasses import fields
from turtle import mode
from rest_framework import serializers
from games import models

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'