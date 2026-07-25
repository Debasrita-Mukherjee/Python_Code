# Parent Class
class Animal:

    def sound(self):
        print("Animals make sound")


# Child Class
class Dog(Animal):

    def bark(self):
        print("Dog barks")


# Creating object
d = Dog()

d.sound()
d.bark()