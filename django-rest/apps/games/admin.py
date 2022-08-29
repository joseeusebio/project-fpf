from unicodedata import category
from django.contrib import admin
from games.models import Game, Company, Category

@admin.register(Game)

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','release_date','get_categories','company','price')
    list_filter = ('category','company')
    search_fields = ('title','category')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('release_date','category','company')
    list_per_page: 5

@admin.register(Company)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page: 5


@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page: 5