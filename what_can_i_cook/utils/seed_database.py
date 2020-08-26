"""
Populates the Django DB with all Ingredients and Recipes. Get called from the migration files.
"""

from pymongo import MongoClient
from what_can_i_cook.models import Recipe, Ingredient, IngredientGroup

client = MongoClient(
    'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wqtbk.mongodb.net/video?retryWrites=true&w=majority')

db = client.recipe_database

recipes = db.recipes


def main():
    """
    Populates the Django DB with all Ingredients and Recipes
    :return: None
    """

    all_recipes = recipes.find({}, {
        "name": 1, "description": 1, "headline": 1, "websiteUrl": 1, "imagePath": 1,
        "ingredients.id": 1, "ingredients.name": 1, "ingredients.family.name": 1, "ingredients.family.id": 1,
        "ingredients.imagePath": 1, "ingredients.shipped": 1})

    for recipe_item in all_recipes:

        ###
        ### 1. Save Recipes:
        ###
        recipe, created = Recipe.objects.get_or_create(
            id=recipe_item["_id"],

            defaults={"name": recipe_item["name"], "description": recipe_item["description"],
                      "websiteUrl": recipe_item["websiteUrl"], "imagePath": recipe_item["imagePath"], })
        if not created:
            print(f"Werk {recipe} gibt es wohl doppelt.")

        ###
        ### 2. Save Ingredients:
        ###

        for ing in recipe_item['ingredients']:
            ing_obj, ing_created = Ingredient.objects.get_or_create(
                id=ing['id'],
                defaults={
                    'name': ing['name'],
                    'shipped': ing['shipped'],
                }
            )
            if ing_created and ing['imagePath']:
                ing_obj.imagePath = ing['imagePath']
                ing_obj.save()

            ###
            ### 3. Save IngredientGroup:
            ###

            if ing_created and 'family' in ing:
                ig, ig_created = IngredientGroup.objects.get_or_create(
                    id=ing['family']['id'],
                    defaults={
                        'name': ing['family']['name'],
                    }
                )

                # Build Ingredient <-> IngredientGroup Relationship
                ig.ingredient_set.add(ing_obj)
                ig.save()

            ###
            ### 4. Build Recepe / Ingredients relationship:
            ###

            if created:
                recipe.ingredients.add(ing_obj)
                recipe.save()
