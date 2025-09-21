from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self):
        self.category = self.make_category(
            name='Category Name',
        )
        return super().setUp()
    
    def test_recipe_category_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name,
            msg='Category string representation must be the same as name field'
        )
    
    def test_recipe_category_name_raises_error_if_more_than_65_chars(self):
        self.category.name = "A" * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()  # Here validation is triggered