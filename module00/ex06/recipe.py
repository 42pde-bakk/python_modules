import sys
import enum


class CMD(enum.IntEnum):
    ADD = 1,
    DELETE = 2,
    PRINT_RECIPE = 3,
    PRINT_COOKBOOK = 4,
    QUIT = 5


def print_menu() -> None:
    print(f'Please select an option by typing the corresponding number:')
    print(f'{CMD.ADD}: Add a recipe')
    print(f'{CMD.DELETE}: Delete a recipe')
    print(f'{CMD.PRINT_RECIPE}: Print a recipe')
    print(f'{CMD.PRINT_COOKBOOK}: Print the cookbook')
    print(f'{CMD.QUIT}: Quit')


def get_input() -> CMD:
    try:
        print_menu()
        user_input = input('>> ')
        print()
        cmd = int(user_input)
        if not (CMD.ADD <= cmd <= CMD.QUIT):
            raise ValueError
        return CMD(cmd)
    except ValueError:
        print(f'This option does not exist, please type the corresponding number.', file=sys.stderr)
        return get_input()


def add_recipe(cookbook: dict):
    try:
        recipe_name = input('>>> Enter a name:\n').strip()
        ingredients = []
        print('>>> Enter ingredients:')
        while True:
            ingredient = input().strip()
            if ingredient:
                ingredients.append(ingredient)
            else:
                break
        assert ingredients, "No recipe can have zero ingredients!"
        food_type = input('>>> Enter a meal type\n').strip()
        assert food_type in ['lunch', 'dessert', 'dinner', 'breakfast'], "Invalid meal type"
        prep_time = input('>>> Enter a preparation time:\n').strip()
        assert prep_time.isdigit(), "Invalid preparation time. Must be in minutes."
        assert int(prep_time) > 0, "Preparation time must be more than zero minutes."
        cookbook[recipe_name] = (ingredients, food_type, int(prep_time))
    except (AssertionError, ValueError) as e:
        print(e, file=sys.stderr)


def delete_recipe(cookbook: dict) -> None:
    recipe_name = input('Please enter a recipe name to delete from the cookbook:\n>> ').strip()

    if recipe_name not in cookbook.keys():
        print('Sorry, this option does not exist.', file=sys.stderr)
        return
    cookbook.pop(recipe_name)


def print_recipe(cookbook: dict) -> None:
    recipe_name = input('Please enter a recipe name to get its details:\n>> ').strip()
    if recipe_name not in cookbook.keys():
        print('Sorry, this option does not exist.', file=sys.stderr)
        return
    ingredients, food_type, duration = cookbook[recipe_name]
    print(f'Recipe for {recipe_name}')
    print(f'\tIngredients list: {ingredients}')
    print(f'\tTo be eaten for {food_type}.')
    print(f'\tTakes {duration} minutes of cooking.\n')


def print_cookbook(cookbook: dict) -> None:
    print(f'Cookbook contains the following recipes:')
    print(', '.join(rec for rec in cookbook.keys()))


def quit_cookbook(cookbook):
    print('Cookbook closed. Goodbye !')
    exit(0)


def init_cookbook() -> dict:
    cookbook = {
        'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10),
        'cake': (['flour', 'sugar', 'eggs'], 'dessert', 60),
        'salad': (['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)
    }
    return cookbook


def loop() -> None:
    funcs = {
        CMD.ADD: add_recipe,
        CMD.DELETE: delete_recipe,
        CMD.PRINT_RECIPE: print_recipe,
        CMD.PRINT_COOKBOOK: print_cookbook,
        CMD.QUIT: quit_cookbook
    }
    cookbook = init_cookbook()
    while True:
        cmd = get_input()
        funcs[cmd](cookbook)


if __name__ == '__main__':
    loop()
