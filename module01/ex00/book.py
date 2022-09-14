from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
        self.__check_values()

    def __check_values(self):
        assert isinstance(self.name, str), 'Name has to be type string'
        assert isinstance(self.last_update, datetime)
        assert isinstance(self.creation_date, datetime)
        assert isinstance(self.recipes_list, dict)
        assert self.name, 'Name cannot be empty'
        assert self.last_update >= self.creation_date

    def get_recipe_by_name(self, name: str):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        print(f'')
        for lst in self.recipes_list:
            for recipe in self.recipes_list[lst]:
                assert isinstance(recipe, Recipe)
                if name == recipe.name:
                    print(recipe)
                    return recipe
        print(f'Sorry, couldn\'t find the recipe for {name}')
        return None

    def get_recipes_by_types(self, recipe_type: str) -> list[Recipe] | None:
        """Get all recipe names for a given recipe_type """
        if recipe_type not in Recipe.ALLOWED_RECIPE_TYPES:
            return None
        if not self.recipes_list[recipe_type]:
            print(f'Sorry, I have no recipes of type {recipe_type}')
        return self.recipes_list[recipe_type]

    # ... Your code here ...
    def add_recipe(self, recipe: Recipe) -> None:
        """Add a recipe to the book and update last_update"""
        if recipe.recipe_type not in Recipe.ALLOWED_RECIPE_TYPES:
            print('Sorry, can\'t add that recipe since the recipe_type is not valid')
            return None
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
