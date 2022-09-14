class Recipe:
    ALLOWED_RECIPE_TYPES = ('starter', 'lunch', 'dessert')

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.__check_values()

    def __check_values(self):
        assert isinstance(self.name, str), 'Name has to be type string'
        assert self.name, 'Name cannot be empty'
        assert isinstance(self.cooking_lvl, int), 'Cooking lvl has to be type int'
        assert 1 <= self.cooking_lvl <= 5, "Cooking lvl has to be between 1 and 5"
        assert isinstance(self.cooking_time, int)
        assert self.cooking_time > 0
        assert isinstance(self.ingredients, list) and self.ingredients
        assert all(isinstance(ingr, str) for ingr in self.ingredients)
        assert isinstance(self.description, str)
        assert isinstance(self.recipe_type, str)
        assert self.recipe_type in Recipe.ALLOWED_RECIPE_TYPES

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe name: " + self.name + '\n\t' \
              + "Cooking level: " + str(self.cooking_lvl) + '\n\t' \
              + "Cooking_time: " + str(self.cooking_time) + " minutes" + '\n\t' + "Ingredients: "
        ingredients = ', '.join(stri for stri in self.ingredients)
        txt += ingredients + '\n\t' + "Description: " + self.description + '\n\t' \
               + "Recipe_type: " + self.recipe_type + '\n'
        return txt
