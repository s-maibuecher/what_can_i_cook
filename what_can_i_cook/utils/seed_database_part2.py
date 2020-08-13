'''
Populates the Ingredients with their Groupname.
'''

from pymongo import MongoClient
from what_can_i_cook.models import Recipe, Ingredient

client = MongoClient(
    'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wqtbk.mongodb.net/video?retryWrites=true&w=majority')

db = client.recipe_database

recipes = db.recipes


def main():
    '''
    Populates the Ingredients with their Groupname.
    :return: None
    '''

    ###
    ### 1. Save Ingredients:
    ###

    # Find ingredients in Mongo DB:
    found_ing_dicts = recipes.find({}, {"ingredients.id": 1, "ingredients.name": 1,
                                        "ingredients.family.name": 1, "_id": 0})

    # Save found ings in model instances:
    for all_ings_for_one_recipe in found_ing_dicts:
        for single_ing_object in all_ings_for_one_recipe["ingredients"]:
            ing = Ingredient.objects.get(pk=single_ing_object['id'])

            if single_ing_object.get('family') and single_ing_object['family'].get('name'):
                ing.group = single_ing_object['family']['name']
                ing.save()
