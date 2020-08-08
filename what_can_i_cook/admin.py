from django.contrib import admin
from what_can_i_cook.models import Recipe, Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('name', 'headline', 'id', 'imagePath', 'description', 'ingredients', 'websiteUrl')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ('name', 'id', 'imagePath', 'shipped')
