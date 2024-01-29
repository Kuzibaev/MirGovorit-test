from django.db import transaction, models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from products.models import Recipe, Product, RecipeIngredient


@transaction.atomic
def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = get_object_or_404(Product, id=product_id)

        recipe_ingredient, created = RecipeIngredient.objects.get_or_create(recipe=recipe, product=product)
        recipe_ingredient.weight_grams = weight
        recipe_ingredient.save()

        return HttpResponse("Product added to recipe successfully.")


@transaction.atomic
def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        recipe = get_object_or_404(Recipe, id=recipe_id)

        RecipeIngredient.objects.filter(recipe=recipe).update(weight_grams=models.F('weight_grams') + 1)
        Product.objects.filter(recipeingredient__recipe=recipe).update(times_used=models.F('times_used') + 1)

        return HttpResponse("Recipe cooked successfully.")


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        recipes_without_product = Recipe.objects.exclude(recipeingredient__product=product)
        recipes_with_less_than_10g = Recipe.objects.filter(recipeingredient__product=product,
                                                           recipeingredient__weight_grams__lt=10)

        context = {
            'recipes_without_product': recipes_without_product,
            'recipes_with_less_than_10g': recipes_with_less_than_10g,
        }

        return render(request, 'show_recipes.html', context)
