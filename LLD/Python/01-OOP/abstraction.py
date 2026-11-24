# =====================================================
#                ABSTRACTION IN PYTHON
# =====================================================

# Definition:
# Abstraction is one of the four main pillars of
# Object-Oriented Programming (OOP).
#
# Abstraction means hiding unnecessary implementation
# details and showing only the essential features
# to the user.
#
# It focuses on WHAT an object does rather than
# HOW it performs the task.
#
#
# Real-Life Example:
# ATM Machine
#
# When we use an ATM machine, we can:
#
# 1. Withdraw Money
# 2. Check Balance
# 3. Deposit Money
#
# We do not need to know how the ATM internally
# communicates with the bank server or processes
# the transaction.
#
# We only use the available features.
#
# This is an example of Abstraction.


# =====================================================
#              ABSTRACT CLASS
# =====================================================

# Definition:
# An Abstract Class is a class that cannot be used
# to create objects directly.
#
# It is mainly used as a blueprint for other classes.
#
# In Python, we use the ABC module to create
# an Abstract Class.
#
# ABC stands for Abstract Base Class.
#
# Syntax:
#
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     pass


# =====================================================
#               ABSTRACT METHOD
# =====================================================

# Definition:
# An Abstract Method is a method that is declared
# inside an Abstract Class but does not contain
# its complete implementation.
#
# The child class must implement all inherited
# abstract methods before its objects can be created.
#
# In Python, we use the @abstractmethod decorator
# to define an Abstract Method.
#
# Example:
#
# @abstractmethod
# def area(self):
#     pass


# =====================================================
#             CONCRETE CLASS
# =====================================================

# Definition:
# A Concrete Class is a normal class that provides
# implementations for all inherited abstract methods.
#
# Objects can be created from a Concrete Class.
#
# Example:
#
# class Rectangle(Shape):
#     def area(self):
#         print("Calculating Area")


# =====================================================
#                PYTHON PROGRAM
# =====================================================

from abc import ABC, abstractmethod


# Abstract Class
class Shape(ABC):

    # Abstract Method
    @abstractmethod
    def area(self):
        pass

    # Abstract Method
    @abstractmethod
    def perimeter(self):
        pass


# =====================================================
#                 CONCRETE CLASS
# =====================================================


class Rectangle(Shape):

    def __init__(self, length: int, breadth: int):

        self.length = length
        self.breadth = breadth

    # Implementing Abstract Method
    def area(self):
        print("Area of Rectangle =", self.length * self.breadth)

    # Implementing Abstract Method
    def perimeter(self):
        print("Perimeter of Rectangle =", 2 * (self.length + self.breadth))


# =====================================================
#                 CREATING OBJECT
# =====================================================

r = Rectangle(5, 10)

# Calling Methods
r.area()
r.perimeter()


# =====================================================
#                      OUTPUT
# =====================================================

# Area of Rectangle = 50
# Perimeter of Rectangle = 30


# =====================================================
#                 EXPLANATION
# =====================================================

# 1. First, we import ABC and abstractmethod
#    from the abc module.
#
# 2. We create an Abstract Class named Shape
#    by inheriting from ABC.
#
# 3. Inside Shape, we define two abstract methods:
#    area() and perimeter().
#
# 4. We use @abstractmethod to declare these methods.
#
# 5. We create a Concrete Class named Rectangle
#    that inherits from Shape.
#
# 6. Rectangle provides implementations for both
#    abstract methods.
#
# 7. We create an object of Rectangle.
#
# 8. Finally, we call area() and perimeter()
#    to calculate the rectangle's area and perimeter.


# =====================================================
#              IMPORTANT RULES OF ABSTRACTION
# =====================================================

# 1. An Abstract Class cannot be instantiated
#    directly.
#
# 2. An Abstract Class can contain both abstract
#    methods and normal methods.
#
# 3. Abstract Methods are declared using
#    the @abstractmethod decorator.
#
# 4. A Concrete Child Class must implement all
#    inherited abstract methods.
#
# 5. If a child class does not implement all
#    abstract methods, it also remains abstract.
#
# 6. We use ABC from the abc module to create
#    Abstract Base Classes.
#
# 7. Abstraction hides implementation details
#    and exposes essential functionality.


# =====================================================
#                ADVANTAGES OF ABSTRACTION
# =====================================================

# 1. Hides unnecessary implementation details.
#
# 2. Makes code easier to understand.
#
# 3. Provides a common blueprint for child classes.
#
# 4. Improves code organization.
#
# 5. Makes large applications easier to maintain.


# =====================================================
#                    CONCLUSION
# =====================================================

# Abstraction is the process of hiding implementation
# details and showing only essential functionality.
#
# REMEMBER:
#
# ABSTRACT CLASS = BLUEPRINT
#
# ABSTRACT METHOD = METHOD WITHOUT COMPLETE
#                   IMPLEMENTATION
#
# CONCRETE CLASS = CLASS THAT IMPLEMENTS
#                  ABSTRACT METHODS
#
# ABC = ABSTRACT BASE CLASS
#
# @abstractmethod = DECORATOR USED TO DECLARE
#                   ABSTRACT METHODS
#
# =====================================================