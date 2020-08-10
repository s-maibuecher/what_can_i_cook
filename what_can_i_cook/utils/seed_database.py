'''
Populates the Django DB with all Ingredients and Recipes. Get called from the migration files.
'''

from pymongo import MongoClient
from what_can_i_cook.models import Recipe, Ingredient

client = MongoClient(
    'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wqtbk.mongodb.net/video?retryWrites=true&w=majority')

db = client.recipe_database

recipes = db.recipes


def main():
    '''
    Populates the Django DB with all Ingredients and Recipes
    :return: None
    '''

    ###
    ### 1. Save Ingredients:
    ###

    # Find ingriedients in Mongo DB:
    found_ing_dicts = recipes.find({}, {"ingredients.id": 1, "ingredients.name": 1,
                                 "ingredients.imagePath": 1, "ingredients.shipped": 1, "_id": 0})

    # Save found ings in model instances:
    for all_ings_for_one_recipe in found_ing_dicts:
        for single_ing_object in all_ings_for_one_recipe["ingredients"]:
            obj, created = Ingredient.objects.get_or_create(
                id=single_ing_object['id'],
                defaults={
                    'name': single_ing_object['name'],
                    'shipped': single_ing_object['shipped'],
                }
            )
            if created and single_ing_object['imagePath']:
                obj.imagePath = single_ing_object['imagePath']
                obj.save()

    ###
    ### 2. Save Recipes:
    ###

    # Find and save recipes in recipe model instances:
    for r in recipes.find({}, {"name": 1, "description": 1, "headline": 1, "websiteUrl": 1,
                               "imagePath": 1, "ingredients.id": 1}):
        recipe, created = Recipe.objects.get_or_create(
            id=r["_id"],
            defaults={"name": r["name"], "description": r["description"],
                      "websiteUrl": r["websiteUrl"], "imagePath": r["imagePath"], })
        if not created:
            print(f"Werk {recipe} gibt es wohl doppelt.")

        else:
            if r["headline"]:
                recipe.headline = r["headline"]

            ###
            ### 3. Build Recepe / Ingredients relationship:
            ###

            for ings in r["ingredients"]:
                recipe.ingredients.add(ings['id'])

            recipe.save()
