from abc import ABC, abstractmethod
"""
Define the abstract base class Animal
"""


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


"""
Define the Dog class inheriting from Animal
"""


class Dog(Animal):

    def sound(self):
        return "Bark"


"""
Define the Cat class inheriting from Animal
"""


class Cat(Animal):

    def sound(self):
        return "Meow"
