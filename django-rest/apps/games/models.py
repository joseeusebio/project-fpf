from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    created_at = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Company(models.Model):
    name = models.CharField(max_length=90, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Game(models.Model):
    title = models.CharField(max_length=60, blank=False, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(max_length=250, default="vazio", blank=True)
    release_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = MoneyField(max_digits=5, decimal_places=2, default_currency='BRL')
    picture = models.ImageField(upload_to='pictures_games/', blank=True)

    class Meta:
        ordering = ('id',)


    def __str__(self) -> str:
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.category = self.category.lower()
        self.company = self.company.lower()
        super(Game, self).save(force_insert, force_update)


    # def get_absolute_url(self):
    #     return reverse('game_detail',
    #             args=[str(self.id)])


    
