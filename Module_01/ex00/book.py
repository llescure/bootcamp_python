from datetime import date
from recipe import Recipe


class Book:
    def __init__(self, name):
        try:
            self.name = str(name)
        except ValueError:
            print("Name is not a string")
            exit()
        self.creation_date = date.today()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name textt{name} and returns the \
                instance"""
        for key, value in self.recipes_list.items():
            for value2 in value:
                if value2.name == name:
                    print("\\texttt {}".format(name))
                    print(value2)
                    exit()
        print("This recipe does not exist")
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        print("All recipe name for {} are:".format(recipe_type))
        for key, value in self.recipes_list.items():
            if recipe_type == key:
                for value2 in value:
                    print(value2.name)

        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        for key, value in self.recipes_list.items():
            if key == recipe.recipe_type:
                value.append(recipe)
                last_update = date.today()
        pass
