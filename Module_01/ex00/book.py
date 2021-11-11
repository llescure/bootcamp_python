from datetime import date
from recipe import Recipe

meals = ["starter", "lunch", "dessert"]

class Book:
    def __init__(self, name):
        try:
            self.name = str(name)
        except:
            print("Name is not a string")
            exit()
        self.last_update = date.today()
        self.creation_date = date.today()

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name textt{name} and returns the instance"""
        for iterator_meals in meals:
            for iterator_recipes in recipes_list[meals]:
                if name == iterator_recipes:
                    print(str(name))
            else:
                print("This recipe doesn't exist")
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for iterator_meals in meals:
            if iterator_meals == recipe_type:
                for iterator_recipes in recipes_list[iterator_meals]:
                    print(str(recipes_list[iterator_meals][iterator_recipes]))

        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        for iterator_meals in meals:
            if iterator_meals == recipe.recipe_type:
               recipes_list[iterator_meals].append(recipe)
        last_update = date.today()
        pass
