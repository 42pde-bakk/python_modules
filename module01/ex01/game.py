class GotCharacter:
    """Class representing a fictional character from Game of Thrones
    (Season 8 was awful)
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Baratheon(GotCharacter):
    """A class representing the Baratheon family"""
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.house_words = 'Ours is the Fury'

    def print_house_words(self) -> None:
        print(self.house_words)

    def die(self) -> None:
        self.is_alive = False
