"""Dog Class

Create a Dog with name and age, a bark() method that prints "<name> says
Woof!", and a birthday() method that increases its age by 1. Create a dog,
call bark(), call birthday() twice, and print the new age.
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1


dog = Dog("Rex", 4)
dog.bark()
dog.birthday()
dog.birthday()
print(f"{dog.name} is now {dog.age} years old.")
