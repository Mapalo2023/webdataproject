import requests
import pandas as pd


class RecipeDataCollector:
    """
    A class to collect recipe data from a specified API.

    Attributes
    ----------
    api_url : str
        The base URL of the recipe API.

    Methods
    -------
    search_by_name(search_term)
        Searches for recipes by name.

    list_by_first_letter(first_letter)
        Lists recipes starting with a specific letter.

    lookup_by_id(recipe_id)
        Looks up a recipe by its ID.

    get_random_meal()
        Retrieves a random meal from the API.

    list_all_categories()
        Lists all recipe categories available in the API.

    list_all_areas()
        Lists all geographical areas of the recipes available in the API.

    filter_by_main_ingredient(main_ingredient)
        Filters recipes by the main ingredient.
    """
    def __init__(self, api_url):
        """
        Constructs all the necessary attributes for the RecipeDataCollector object.

        Parameters
        ----------
        api_url : str
            The base URL of the recipe API.
        """
        self.api_url = api_url

    def search_by_name(self, search_term):
        """
        Searches for recipes by name.

        Parameters
        ----------
        search_term : str
            The search term to look for in recipe names.

        Returns
        -------
        DataFrame
            A pandas DataFrame containing the found recipes.

        Raises
        ------
        ValueError
            If no recipes are found for the given search term.
        """
        response = requests.get(f"{self.api_url}/api/json/v1/1/search.php?s={search_term}")
        data = response.json()

        if 'meals' not in data:
            raise ValueError("No recipes found for the given search term.")

        recipes = data['meals']
        recipe_data = []

        for recipe in recipes:
            id = recipe['idMeal']
            name = recipe['strMeal']
            area = recipe['strArea']
            category = recipe['strCategory']
            instructions = recipe['strInstructions']
            image_url = recipe['strMealThumb']

            recipe_data.append({
                'id': id,
                'name': name,
                'area': area,
                'category': category,
                'instructions': instructions
            })

        return pd.DataFrame(recipe_data)

    def list_by_first_letter(self, first_letter):
        """
        Lists recipes that start with a specific letter.

        Parameters
        ----------
        first_letter : str
            The first letter of the recipe names to search for.

        Returns
        -------
        DataFrame
            A pandas DataFrame containing the found recipes.

        Raises
        ------
        ValueError
            If no recipes are found starting with the given letter.
        """
        response = requests.get(f"{self.api_url}/api/json/v1/1/search.php?f={first_letter}")
        data = response.json()

        if 'meals' not in data:
            raise ValueError("No recipes found starting with the given letter.")

        recipes = data['meals']
        recipe_data = []

        for recipe in recipes:
            id = recipe['idMeal']
            name = recipe['strMeal']
            area = recipe['strArea']
            category = recipe['strCategory']
            instructions = recipe['strInstructions']
            image_url = recipe['strMealThumb']

            recipe_data.append({
                'id': id,
                'name': name,
                'area': area,
                'category': category,
                'instructions': instructions
            })

        return pd.DataFrame(recipe_data)

    def lookup_by_id(self, recipe_id):
        """
        Looks up a recipe by its ID.

        Parameters
        ----------
        recipe_id : str
            The ID of the recipe to look up.

        Returns
        -------
        dict
            A dictionary containing details of the found recipe.

        Raises
        ------
        ValueError
            If no recipe is found with the given ID.
        """
        response = requests.get(f"{self.api_url}/api/json/v1/1/lookup.php?i={recipe_id}")
        data = response.json()

        if 'meals' not in data:
            raise ValueError("No recipe found with the given ID.")

        recipe = data['meals'][0]
        recipe_data = {
            'id': recipe['idMeal'],
            'name': recipe['strMeal'],
            'area': recipe['strArea'],
            'category': recipe['strCategory'],
            'instructions': recipe['strInstructions']
        }

        for ingredient in range(20):
            if f"strIngredient{ingredient + 1}" in recipe:
                ingredient_name = recipe[f"strIngredient{ingredient + 1}"]
                ingredient_measure = recipe[f"strMeasure{ingredient + 1}"]
                recipe_data[ingredient_name] = ingredient_measure

        return recipe_data

    def get_random_meal(self):
        """
        Retrieves a random meal from the API.

        Returns
        -------
        dict
            A dictionary containing details of the random meal.
        """
        response = requests.get(f"{self.api_url}/api/json/v1/1/random.php")
        data = response.json()

        recipe = data['meals'][0]
        recipe_data = {
            'id': recipe['idMeal'],
            'name': recipe['strMeal'],
            'area': recipe['strArea'],
            'category': recipe['strCategory'],
            'instructions': recipe['strInstructions']
        }

        for ingredient in range(20):
            if f"strIngredient{ingredient + 1}" in recipe:
                ingredient_name = recipe[f"strIngredient{ingredient + 1}"]
                ingredient_measure = recipe[f"strMeasure{ingredient + 1}"]
                recipe_data[ingredient_name] = ingredient_measure

        return recipe_data
    
    def list_all_categories(self):
        """
        Lists all recipe categories available in the API.

        Returns
        -------
        DataFrame
            A pandas DataFrame containing all recipe categories.

        Raises
        ------
        ValueError
            If no categories are found.
        """
        response = requests.get(f"{self.api_url}/api/json/v1/1/categories.php")
        data = response.json()

        if 'categories' not in data:
            raise ValueError("No categories found.")

        categories = data['categories']
        category_data = []

        for category in categories:
            category_data.append({
            'id': category['idCategory'],
            'name': category['strCategory'],
            'description': category['strCategoryDescription']
        })

        return pd.DataFrame(category_data)
    


    



