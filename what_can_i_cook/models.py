from django.db import models
from django.db.models import Count


class Ingredient(models.Model):
    '''
    Strongly simplified model of hellofresh ingredients
    '''
    id = models.CharField(primary_key=True, max_length=24)

    name = models.CharField(max_length=100)

    group = models.CharField(max_length=100, blank=True)

    imagePath = models.CharField(max_length=100)

    shipped = models.BooleanField()

    @property
    def image_url(self):
        return 'https://img.hellofresh.com/f_auto,fl_lossy,h_100,q_auto,w_100/hellofresh_s3/' + self.imagePath

    class Meta:
        verbose_name = 'Ingredient'

    def __str__(self):
        return f'Ingredient <ID: {self.id}>: {self.name}'


class RecipeManager(models.Manager):
    '''
    There are round about ~160 recipes which contains no ingredients
    '''
    def get_queryset(self):
        return super().get_queryset().annotate(ing_counter=Count('ingredients')).filter(ing_counter__gt=1)


class Recipe(models.Model):
    '''
    Strongly simplified model of hellofresh Recipes
    '''
    id = models.CharField(primary_key=True, max_length=24)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    headline = models.CharField(max_length=200)

    websiteUrl = models.URLField()

    ingredients = models.ManyToManyField(to=Ingredient)

    imagePath = models.CharField(max_length=100)

    @property
    def image_url(self):
        return 'https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_200,q_auto,w_420/hellofresh_s3' + self.imagePath

    downloaded_img = models.ImageField(blank=True)  # todo https://stackoverflow.com/a/16174886/2952486

    objects = models.Manager()  # The default manager.
    valuable_recipes = RecipeManager()  # filters recipes with too less ingredients

    class Meta:
        verbose_name = 'Recipe'

    def __str__(self):
        return f'Recipe <ID: {self.id}>: {self.name}'
