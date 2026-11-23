class Animal: # parent
    def __init__(self,name : str,age:int)-> None :
        self.name = name
        self.age = age 
        
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Dog(Animal): #child
    def __init__(self, name:str, age:int ,breed:str)-> None:
        super().__init__(name, age) # super help to use it parent 
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"Age is {self.age} and name is {self.name},breed is {self.breed}")

dog = Dog("trapu", 4, "haski")

dog.bark()
dog.eat()
dog.sleep()
dog.display()

# animal = Animal()
# animal.sleep()
# animal.eat()

"""
# ==================================================
#              INHERITANCE IN PYTHON
# ==================================================

# 1. WHAT IS INHERITANCE?
#
# Inheritance is one of the four main pillars of OOP.
#
# It allows one class to acquire the attributes and
# methods of another class.
#
# It promotes code reusability and avoids code duplication.
#
# Parent Class = Base Class
# Child Class  = Derived Class


# 2. PARENT CLASS AND CHILD CLASS
#
# Parent Class:
# A class whose attributes and methods are inherited
# by another class.
#
# Child Class:
# A class that inherits attributes and methods
# from another class.
#
# SYNTAX:
#
# class ChildClass(ParentClass):
#     pass
#
# EXAMPLE:
#
# class Animal:       # Parent class
#     pass
#
# class Dog(Animal):  # Child class
#     pass
#
# Here, Dog inherits from Animal.


# 3. WHY DO WE USE INHERITANCE?
#
# - Code reusability.
# - Avoids code duplication.
# - Makes code easier to maintain.
# - Allows us to extend existing functionality.
# - Establishes relationships between classes.


# 4. TYPES OF INHERITANCE
#
# Python supports five main types of inheritance.
#
# 1. SINGLE INHERITANCE
# One child class inherits from one parent class.
#
#       Animal
#          |
#         Dog
#
#
# 2. MULTIPLE INHERITANCE
# One child class inherits from multiple parent classes.
#
#       Father    Mother
#           \     /
#            Child
#
#
# 3. MULTILEVEL INHERITANCE
# A class inherits from another derived class,
# forming a chain of inheritance.
#
#       Animal
#          |
#         Dog
#          |
#        Puppy
#
#
# 4. HIERARCHICAL INHERITANCE
# Multiple child classes inherit from one parent class.
#
#          Animal
#          /    \
#        Dog    Cat
#
#
# 5. HYBRID INHERITANCE
# A combination of two or more types of inheritance.


# 5. CONSTRUCTOR IN INHERITANCE (__init__)
#
# __init__() is a special method called a constructor.
#
# It is automatically called when an object is created.
#
# It is generally used to initialize object attributes.
#
# IMPORTANT:
#
# - If a child class does not define its own __init__(),
#   it can use the parent's constructor.
#
# - If a child class defines its own __init__(),
#   the parent's constructor is not automatically called.
#
# - We use super() to call the parent's constructor.


# 6. WHAT IS super()?
#
# super() is a built-in function used to access methods
# and constructors from the parent class through MRO.
#
# EXAMPLE:
#
# super().__init__(name, age)
#
# This calls the parent's __init__() method and initializes
# the attributes defined in the parent class.
#
# BENEFITS:
#
# - Avoids rewriting parent initialization code.
# - Promotes code reusability.
# - Helps maintain inheritance relationships.
# - Supports cooperative multiple inheritance.


# 7. ACCESSING PARENT CLASS METHODS
#
# A child class can directly access inherited methods
# and attributes from its parent class.
#
# EXAMPLE:
#
# dog.eat()
#
# If eat() belongs to Animal and Dog inherits Animal,
# the Dog object can call eat().


# 8. CHILD CLASS METHODS AND ATTRIBUTES
#
# A child class can have its own methods and attributes
# in addition to the inherited ones.
#
# EXAMPLE:
#
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
#
# Here:
# name and age are initialized by the parent constructor.
# breed is an additional child class attribute.


# 9. METHOD OVERRIDING
#
# When a child class defines a method with the same name
# as a method in its parent class, it is called
# Method Overriding.
#
# The child's version is executed when called through
# an object of the child class.
#
# EXAMPLE:
#
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
# dog = Dog()
# dog.sound()
#
# OUTPUT:
# Dog barks
#
# Method overriding allows a child class to provide
# its own implementation of an inherited method.


# 10. METHOD RESOLUTION ORDER (MRO)
#
# MRO determines the order in which Python searches
# for methods and attributes in an inheritance hierarchy.
#
# It is especially important in multiple inheritance.
#
# We can check MRO using:
#
# print(Dog.mro())
#
# OR
#
# print(Dog.__mro__)


# 11. IMPORTANT POINTS TO REMEMBER
#
# - A child class inherits from its parent class.
# - A child class can access inherited methods and attributes.
# - A child class can have its own methods and attributes.
# - A child class can override parent class methods.
# - super() helps access parent class functionality.
# - A parent class does not inherit from its child class.
# - Inheritance promotes code reusability.
# - Python supports five main types of inheritance.


# ==================================================
#              PRACTICAL EXAMPLE
#               SINGLE INHERITANCE
# ==================================================

class Animal:  # Parent class

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):  # Child class

    def __init__(self, name: str, age: int, breed: str) -> None:

        # Calling the parent class constructor
        super().__init__(name, age)

        # Initializing the child class attribute
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Breed: {self.breed}"
        )


# Creating an object of the Dog class
dog = Dog("Trapu", 4, "Husky")

# Calling the child class method
dog.bark()

# Calling inherited parent class methods
dog.eat()
dog.sleep()

# Accessing parent and child class attributes
dog.display()


# OUTPUT:
#
# I am barking
# I am eating
# I am sleeping
# Name: Trapu, Age: 4, Breed: Husky


# ==================================================
#               END OF INHERITANCE
# ==================================================

"""
