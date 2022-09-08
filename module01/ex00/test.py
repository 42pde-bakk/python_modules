from book import Book
from recipe import Recipe


if __name__ == '__main__':
    myBook = Book("myBook")
    Speculaascake = Recipe("Speculaascake", 3, 45, ["Speculaas", "butter", "milk", "eggs", "sugar"],
                            "Nice cake to eat during sinterklaas time", "dessert")
    Pasta = Recipe("Pasta", 1, 20, ["Literally", "Just", "Pasta"], "", "starter")
    myBook.add_recipe(Speculaascake)
    myBook.add_recipe(Pasta)
    myBook.get_recipe_by_name('Speculaascake')
    res = myBook.get_recipes_by_types('starter')
    for a in res:
        print(a)
