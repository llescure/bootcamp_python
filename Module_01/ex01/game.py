class GotCharacter:
    """Define characters of Game of Thrones"""
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = True


class Targaryen(GotCharacter):
    """A class representing the Targaryen family. Or when its members \
ultimatelly go mad."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and blood"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to \
good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
