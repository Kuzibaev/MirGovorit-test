from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    times_used = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Product, through='RecipeIngredient')

    def __str__(self):
        return self.recipe_name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight_grams = models.IntegerField()

    def __str__(self):
        return f'{self.product.product_name} ({self.weight_grams}g)'
