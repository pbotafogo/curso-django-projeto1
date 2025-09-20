
from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:  # não cria mais receita automaticamente
        return super().setUp()

    def make_category(self, name="Category"):
        return Category.objects.create(name=name)

    def make_author(
        self,
        username='username',
        first_name='First',
        last_name='Last',
        password='newpassword',
        email='newuser@example.com'
    ):
        return User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )

    def make_recipe(
        self,
        title='Another Test Recipe',
        category_data=None,
        author_data=None,
        description='Another Test Description',
        slug='another-test-recipe',
        preparation_time=15,
        preparation_time_unit='Minutes',
        preparation_servings=4,
        preparation_servings_unit='People',
        preparation_steps='Another Test Steps',
        is_published=True,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            preparation_servings=preparation_servings,
            preparation_servings_unit=preparation_servings_unit,
            preparation_steps=preparation_steps,
            is_published=is_published
        )
