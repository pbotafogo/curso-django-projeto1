from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Test Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutes',
            preparation_servings=2,
            preparation_servings_unit='People',
            preparation_steps='Recipe Preparation Steps',
            # is_published=True,  # Even if we set True
            # preparation_steps_is_html=True,  # Even if we set True
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_title_raises_error_if_more_than_65_chars(self):
        self.recipe.title = "A" * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()  # Here validation is triggered

    @parameterized.expand([
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 65),
            ("preparation_servings_unit", 65),
        ])
    def test_recipe_fields_max_length(self, field, max_length):
        """Test if fields have the correct max_length"""
        setattr(self.recipe, field, "A" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_is_published_is_false_by_default(self):   
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False by default')

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):   
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False by default')

    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe),
            needed,
            msg=f'Expected "{needed}" but got "{str(self.recipe)}"'
        )
