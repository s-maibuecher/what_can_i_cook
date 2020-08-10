'''
Little Helper File to seed the Mongo Atlas DB with recipe data:
Have to run only once.
'''

from pymongo import MongoClient
import json, os

RECIPES_FOLDER = '../../recipes'

client = MongoClient(
    'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wqtbk.mongodb.net/video?retryWrites=true&w=majority')

db = client.recipe_database

recipes = db.recipes

recipes_files = [file for file in os.listdir(RECIPES_FOLDER) if file.endswith('.json')]

for recipe in recipes_files:
    PATH_TO_FILE = os.path.abspath(os.path.join(RECIPES_FOLDER, recipe))

    with open(PATH_TO_FILE, "r") as file:
        jfile = json.load(file)

    items = jfile["items"]

    for i in items:
        i['_id'] = i.pop('id') # Mongo DB Konvention

    result = recipes.insert_many(items, ordered=False)


