from enum import Enum

class Type(Enum):
    NONE = 0
    X = 1
    O = 2

class Piece:
    def __init__(self):
        self._type = Type.NONE
        self.age = 0

    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t

    def get_age(self):
        return self.age

    def set_age(self, n):
        self.age = n

    def lose_age(self):
        if self.age != 0:
            self.age -= 1
        if self.age == 0:
            self.set_type(Type.NONE)

    def __eq__(self, other):
        return self._type == other.get_type() and self._type != Type.NONE

    def __ne__(self, other):
        return not self.__eq__(other)