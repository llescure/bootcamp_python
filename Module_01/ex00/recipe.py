class Recipe:
    """Recipe's characteristics"""
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        is_str = isinstance(name, str)
        if is_str:
            self.name = str(name)
        else:
            print("Name is not a string")
            exit()
        try:
            self.cooking_lvl = int(cooking_lvl)
        except ValueError:
            print("cooking_lvl is not an integer")
            exit()
        else:
            if 0 <= cooking_lvl > 5:
                print("cooking_lvl is out of range")
                exit()
        try:
            self.cooking_time = int(cooking_time)
        except ValueError:
            print("cooking_time is not an integer")
            exit()
        else:
            if cooking_time < 0:
                print("cooking_time can't be negative")
                exit()
        try:
            self.ingredients = list(ingredients)
        except ValueError:
            print("Ingredients given is not a list")
            exit()
        is_description_str = isinstance(description, str)
        if is_description_str:
            self.description = str(description)
        else:
            print("Description is not a string")
            exit()
        is_recipe_type_str = isinstance(recipe_type, str)
        if is_recipe_type_str:
            self.recipe_type = str(recipe_type)
        else:
            print("Description is not a string")
            exit()
        if recipe_type is not "starter" and recipe_type is not "lunch" \
                and recipe_type is not "dessert":
            print("Recipe_type must be either starter, lunch or dessert")
            exit()

    def __repr__(self):
        return "Today you will learn how to make a {}.\n\
It is a {}.\n\
You need to have a cooking level of {}.\n\
It will take you {} minutes to prepare.\n\
You need the following ingredients: {}.\n\
{}".format(self.name, self.recipe_type, self.cooking_lvl,
           self.cooking_time, self.ingredients, self.description)

    def __str__(self):
        txt = "Today you will learn how to make a {}.\n\
It is a {}.\n\
You need to have a cooking level of {}.\n\
It will take you {} minutes to prepare.\n\
You need the following ingredients: {}.\n\
{}".format(self.name, self.recipe_type, self.cooking_lvl,
           self.cooking_time, self.ingredients, self.description)
        return txt
