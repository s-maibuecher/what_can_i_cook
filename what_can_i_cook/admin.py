from django.contrib import admin
from what_can_i_cook.models import Recipe, Ingredient, IngredientGroup

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')
    fields = ('name', 'headline', 'id', 'imagePath', 'description', 'ingredients', 'websiteUrl')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')
    fields = ('name', 'id', 'imagePath', 'group', 'shipped')

@admin.register(IngredientGroup)
class IngredientGroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'id')
