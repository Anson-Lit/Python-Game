class Player:
    def __init__(self, backpack) -> None:
        """Initializing attributes"""
        self.backpack = backpack


    @property
    def backpack(self):
        return self._backpack
    @backpack.setter
    def backpack(self, value):
        self._backpack = value
    #backpack attribute will eventually be a list that stores all items collected