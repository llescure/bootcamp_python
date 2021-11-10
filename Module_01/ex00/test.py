from recipe import Recipe
from book import Book

porridge = Recipe("porridge", 2, 5, ["oat", "milk", "honey", "hazelnuts"], \
        "Put the desired amount of oat in a bowl. Pour the milk \
above. Put in the microwave for 1.30 minutes. Add some honey and \
hazenuts. Your porridge is now ready to be eaten.", "dessert")
to_print = str(porridge)
print(to_print)

first_book = Book("Easy to do")

first_book.get_recipe_by_name(porridge)

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
