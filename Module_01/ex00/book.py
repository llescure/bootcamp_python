from datetime import date
from recipe import Recipe

class Book:
    def __init__(self, name):
        try:
            self.name = str(name)
        except:
            print("Name is not a string")
            exit()
        self.creation_date = date.today()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": None, "lunch": None, "dessert": None}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name textt{name} and returns the instance"""
        for key, value in self.recipes_list.items():
            if value != None:
                if value.name == name:
                    print(value)
                else:
                    print("This recipe does not exist")
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key, value in self.recipes_list.items():
            if key == recipe_type:
                print(value)

        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        for key, value in self.recipes_list.items():
            if key == recipe.recipe_type:
               self.recipes_list[key] = recipe
        last_update = date.today()
        pass
