#!/usr/bin/python3


class Dog():
    """A dog modelling attempt"""
    def __init__(self, name, age):
        """Initializing name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """simulation of a dog sitting after a command"""
        print(self.name + "is now sitting.")

    def roll_over(self):
        """simulation of dog rolling over after a command"""
        print(self.name + "rolled over.")

    my_dog = Dog('Zap', 4)
    print("My dog's name is " + my_dog.name + ".")
    print("My dog is " + str(my_dog.age) + "'years old.")
