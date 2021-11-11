from recipe import Recipe
from book import Book

porridge = Recipe("porridge", 2, 5, ["oat", "milk", "honey", "hazelnuts"], \
        "Put the desired amount of oat in a bowl. Pour the milk \
above. Put in the microwave for 1.30 minutes. Add some honey and \
hazenuts. Your porridge is now ready to be eaten.", "dessert")
tomatoes_salad = Recipe("tomatoes salad", 1, 5, ["tomatoes", "vinegar", "oil",\
"mustard"], "Take three tomatoes and cut them vertically in slices. Take a bowl. \
Put two spoons of oil and one spoon of vinegar. Add a little bit of mustard.\
Pour the sauce on your tomatoes. Enjoy your tomatoes salad", "starter")
boiled_eggs = Recipe("boiled eggs", 2, 5, ["eggs", "mayonaise"], \
"Take two eggs and put them for four minutes in boiling water \
Peel away the shell. Cut them in half and add mayonaise on the top\
Enjoy your boiled eggs", "starter")
to_print = str(porridge)
print(to_print)

first_book = Book("Easy to do")

first_book.add_recipe(porridge)
first_book.add_recipe(tomatoes_salad)
first_book.add_recipe(boiled_eggs)
first_book.get_recipes_by_types("starter")
#first_book.get_recipe_by_name("tomatoes salad")

# Test error cases

"""print()

porridge_failed3 = Recipe("porridge", 2, 5, ["oat", "milk", "honey", "hazelnuts"], \
        "Put the desired amount of oat in a bowl. Pour the milk \
above. Put in the microwave for 1.30 minutes. Add some honey and \
hazenuts. Your porridge is now ready to be eaten.", "dinner")
to_print = str(porridge_failed3)
print(to_print)

print()

porridge_failed1 = Recipe("porridge", "a", 5, ["oat", "milk", "honey", "hazelnuts"], \
        "Put the desired amount of oat in a bowl. Pour the milk \
above. Put in the microwave for 1.30 minutes. Add some honey and \
hazenuts. Your porridge is now ready to be eaten.", "dessert")
to_print = str(porridge_failed1)
print(to_print)

print()

porridge_failed2 = Recipe(1, 2, 5, ["oat", "milk", "honey", "hazelnuts"], \
        "Put the desired amount of oat in a bowl. Pour the milk \
above. Put in the microwave for 1.30 minutes. Add some honey and \
hazenuts. Your porridge is now ready to be eaten.", "dessert")
to_print = str(porridge_failed2)
print(to_print)"""
