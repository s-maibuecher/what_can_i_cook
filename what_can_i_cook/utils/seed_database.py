from pymongo import MongoClient
from what_can_i_cook.models import Recipe, Ingredient

client = MongoClient(
    'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wqtbk.mongodb.net/video?retryWrites=true&w=majority')

db = client.recipe_database

recipes = db.recipes


def main():
    # Zutaten finden:
    rec_ings = recipes.find({}, {"ingredients.id": 1, "ingredients.name": 1,
                                 "ingredients.imagePath": 1, "ingredients.shipped": 1, "_id": 0})

    # gefundene Zutaten abspeichern
    for ings in rec_ings:
        for ri in ings["ingredients"]:
            obj, created = Ingredient.objects.get_or_create(
                id=ri['id'],
                defaults={
                    'name': ri['name'],
                    'shipped': ri['shipped'],
                }
            )
            if created and ri['imagePath']:
                obj.imagePath = ri['imagePath']
                obj.save()

    # Rezepte finden und speichern:
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

            # Rezete / Zutaten Beziehungen:
            for i in r["ingredients"]:
                recipe.ingredients.add(i['id'])

            recipe.save()
