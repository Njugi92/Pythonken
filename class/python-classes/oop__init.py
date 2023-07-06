#!/usr/bin/python3


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hallo, how are you", self.name)


p = Person("karuma")
p.say_hi()
