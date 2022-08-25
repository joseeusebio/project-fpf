from distutils.command.upload import upload
from tabnanny import verbose
import uuid
from django.db import models
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    created_at = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Company(models.Model):
    name = models.CharField(max_length=90, primary_key=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Game(models.Model):
    id_game = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60, blank=False)
    description = models.TextField(max_length=250, default="vazio", blank=True)
    release_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = MoneyField(max_digits=5, decimal_places=2, default_currency='BRL')
    picture = models.ImageField(upload_to='pictures_games/', blank=True)

    class Meta:
        ordering = ('-release_date','price',)
