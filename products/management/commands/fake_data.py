from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product, Recipe, RecipeIngredient

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def handle(self, *args, **options):
        for _ in range(10):
            Product.objects.create(
                product_name=fake.word(),
                times_used=fake.random_int(min=0, max=100)
            )

        for _ in range(5):
            recipe = Recipe.objects.create(
                recipe_name=fake.sentence()
            )

            for _ in range(3):
                product = Product.objects.order_by('?').first()
                RecipeIngredient.objects.create(
                    recipe=recipe,
                    product=product,
                    weight_grams=fake.random_int(min=10, max=200)
                )

        self.stdout.write(self.style.SUCCESS('Fake data has been generated successfully.'))
