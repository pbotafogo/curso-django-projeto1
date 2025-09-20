from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # @skip("WIP")
    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here', response.content.decode('utf-8'))
        # I have to write more things here about this test
        # make the test fail:
        # self.fail("Finish this test")

    def test_recipe_home_templates_loads_recipes(self):
        # Create a recipe to test if it appears on the homepage
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        # check if one recipe exists
        self.assertIn('Another Test Recipe', content)
        self.assertEqual(len(response_context_recipes), 1)
        ...

    def test_recipe_category_view_returns_status_code_200(self):
        # Create a recipe to ensure the category exists
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(True)

    def test_recipe_category_view_returns_status_code_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templates_loads_recipes(self):
        needed_title = 'This is a category test'
        # Create a recipe to test if it appears on the category page
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        # check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 250}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_templates_load_the_correct_recipe(self):
        needed_title = 'This is a detail page - it loads one recipe'
        # Create a recipe to test if it appears on the detail page
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:recipe',
                                           kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        # check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_home_template_dont_load_non_published_recipes(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here', response.content.decode('utf-8'))

    def test_recipe_category_template_dont_load_non_published_recipes(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:category', 
                                           kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_dont_load_non_published_recipes(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', 
                                           kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
