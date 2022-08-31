from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    created_at = models.DateField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Category, self).save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=90, unique=True)
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Company, self).save(*args, **kwargs)


class Game(models.Model):
    title = models.CharField(max_length=60, blank=False, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=False)
    description = models.TextField(max_length=250, default="vazio", blank=True)
    release_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = MoneyField(max_digits=5, decimal_places=2, default_currency='BRL')
    quantity = models.PositiveIntegerField()
    is_activate = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures_games/', null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Game, self).save(*args, **kwargs)

    # def get_categories(self):
    #     return ",".join([str(i) for i in self.category.all()])

    # def get_absolute_url(self):
    #     return reverse('game_detail',
    #             args=[str(self.id)])


    
