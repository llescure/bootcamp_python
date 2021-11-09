import sys


cookbook = {
        'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                     'meal': 'lunch', 'time': '10 minutes'},
        'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                 'meal': 'dessert', 'time': '60 minutes'},
        'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                  'meal': 'lunch', 'time': '15 minutes'}
}


def print_cookbook(recipe):
    for name, recipe_info in cookbook.items():
        if name == recipe:
            print("")
            print("Recipe for " + name + ":")
            print("Ingredients list:", recipe_info["ingredients"])
            print("To be eaten for " + recipe_info["meal"] + ".")
            print("Takes " + recipe_info["time"] + " of cooking.\n")
            return
    print("This recipe does not exist, please type an existing recipe or add" +
          "a new one.")
    print("To exit, enter 5\n")


def delete_from_cookbook(recipe):
    for name, recipe_info in cookbook.items():
        if name == recipe:
            del cookbook[recipe]
            print("")
            return
    print("This recipe does not exist, please type an existing recipe or add" +
          "a new one.")
    print("To exit, enter 5\n")


def add_in_cookbook(recipe, ingredients, meal, time):
    cookbook[recipe] = {}

    formatted_ingredients = ingredients.split(', ')
    cookbook[recipe]['ingredients'] = formatted_ingredients
    cookbook[recipe]['meal'] = meal
    cookbook[recipe]['time'] = time
    print("")


def print_all_cookbook():
    for name, recipe_info in cookbook.items():
        print_cookbook(name)


if len(sys.argv) == 1:
    while 1:
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        try:
            value = int(input())
            if value == 1:
                recipe = input("\nPlease enter the recipe's name you want to"
                               "add: \n")
                ingredients = input("Please enter its ingredients(Usage: "
                                    "ingredient1, ingredient2, ...)\n")
                meal = input("Please enter its meal type\n")
                time = input("Please enter its preparation time in minutes"
                             "(Example: 10 minutes)\n")
                add_in_cookbook(recipe, ingredients, meal, time)
            elif value == 2:
                recipe = input("\nPlease enter the recipe's name you want to"
                               "delete: \n")
                delete_from_cookbook(recipe)
            elif value == 3:
                recipe = input("\nPlease enter the recipe's name to get its"
                               "details: \n")
                print_cookbook(recipe)
            elif value == 4:
                print_all_cookbook()
            elif value == 5:
                break
            else:
                print("\nThis option does not exist, please type the " +
                      "corresponding number.")
                print("To exit, enter 5.\n")
        except ValueError:
            print("\nThis option does not exist, please type the " +
                  "corresponding number.")
            print("To exit, enter 5.\n")
else:
    print("Wrong usage please use python3 recipe.py")
