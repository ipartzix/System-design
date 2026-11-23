class Student:
    # Attributes :- variables inside the class are called attributes
    # name = ""
    # age = 0
    # gender = ""


    # methods 
    def __init__ (self, name:str,age:int, gender:str )->None:
        print("================================")
        print("this is a constructor or initilizer ")
        self.name = name
        self.age = age
        self.gender = gender
                


    # def set_info(self , n: str ,a : int, g:str):
    #     # self.name = input("Enter your Name :")
    #     # self.age = input("Enter your age :")
    #     # self.gender = input("Enter your gender :")
    #     # self.name = n
    #     # self.age = a
    #     # self.gender = g
        

    def display(self)-> None:
        print(f"My name is {self.name }. age is {self.age} my gender is {self.gender} ")

    def get_age(self):
        return self.age

# ======== Set the data =========

s1 = Student("partha", 21 , "male")
# s1.set_info("Partha",21 , "male")
s1.display()
print(s1.get_age())

# s2 = Student()
# s2.set_info("ram", 33 ,"male")
# s2.display()


"""
============================================================
                PYTHON: CLASS AND OBJECT
============================================================

1. WHAT IS A CLASS?
-------------------
A class is a blueprint or template used to create objects.

It defines the attributes (variables) and methods (functions)
that an object will have.

Syntax:

class ClassName:
    # Attributes
    # Methods
    pass


2. WHAT IS AN OBJECT?
---------------------
An object is an instance of a class.

In simple words:
    Class  = Blueprint or design
    Object = Real instance created using that blueprint

Example:
    s1 = Student()

Here:
    Student is the class.
    s1 is the object of the Student class.

We can create multiple objects from one class:
    s1 = Student()
    s2 = Student()
    s3 = Student()


3. WHAT ARE ATTRIBUTES?
-----------------------
Attributes are variables defined inside a class that store
data or represent the properties of an object.

Example:

class Student:
    name = ""
    age = 0
    gender = ""

Here:
    name   = Attribute
    age    = Attribute
    gender = Attribute


4. WHAT ARE METHODS?
--------------------
Methods are functions defined inside a class.

They represent the behaviours or actions of an object.

Example:

class Student:
    def display(self):
        print("Hello Student")

Here:
    display() is a method.

We can call it using an object:
    s1 = Student()
    s1.display()


5. WHAT IS A CONSTRUCTOR (__init__)?
------------------------------------
A constructor is a special method that runs automatically
when an object is created.

In Python, __init__() is used to initialize an object's
attributes with values.

Example:

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

Creating an object:

s1 = Student("Partha", 21, "male")

When the object is created, __init__() is called
automatically and initializes the object's attributes.


6. WHAT IS self?
----------------
self refers to the current object of the class.

It is used to access the attributes and methods of the
current object.

Example:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

Here:
    self.name refers to the name of the current object.
    self.age refers to the age of the current object.

NOTE:
self is not a Python keyword. It is a naming convention
that is strongly recommended.


7. WHAT IS A GETTER METHOD?
---------------------------
A getter method is used to retrieve or read the value
of an object's attribute.

Example:

def get_age(self):
    return self.age

Calling the method:
    print(s1.get_age())

It returns the age of the student.


8. WHAT IS A SETTER METHOD?
---------------------------
A setter method is used to modify or update the value
of an object's attribute.

Example:

def set_age(self, age):
    self.age = age

Calling the method:
    s1.set_age(25)

It updates the age of the student to 25.


9. UNDERSTANDING THE STUDENT CLASS
----------------------------------

class Student:

    # Constructor / Initializer
    def __init__(self, name: str, age: int,
                 gender: str) -> None:

        print("================================")
        print("This is a constructor or initializer")

        self.name = name
        self.age = age
        self.gender = gender

    # Display method
    def display(self) -> None:
        print(
            f"My name is {self.name}. "
            f"Age is {self.age}. "
            f"My gender is {self.gender}"
        )

    # Getter method
    def get_age(self):
        return self.age


# Creating an object
s1 = Student("Partha", 21, "male")

# Calling methods
s1.display()
print(s1.get_age())


10. MULTIPLE OBJECTS FROM ONE CLASS
-----------------------------------

We can create multiple objects from a single class.
Each object maintains its own instance attributes.

Example:

s1 = Student("Partha", 21, "male")
s2 = Student("Ram", 33, "male")
s3 = Student("Rahul", 25, "male")

Here:
    s1 stores Partha's information.
    s2 stores Ram's information.
    s3 stores Rahul's information.

All three objects belong to the Student class.


11. DIFFERENCE BETWEEN CLASS AND OBJECT
---------------------------------------

CLASS:
    1. A blueprint or template.
    2. Defines attributes and methods.
    3. Declared using the class keyword.
    4. Example: Student

OBJECT:
    1. An instance of a class.
    2. Has its own instance attributes.
    3. Created by calling the class.
    4. Example: s1 = Student()


12. IMPORTANT TERMS
-------------------

Class       : Blueprint for creating objects.
Object      : Instance of a class.
Attribute   : Variable inside a class.
Method      : Function inside a class.
Constructor : Special initializer method (__init__).
self        : Reference to the current object.
Getter      : Method used to retrieve attribute values.
Setter      : Method used to modify attribute values.
Instance    : An object created from a class.


13. IMPORTANT POINTS TO REMEMBER
--------------------------------

1. A class is created using the class keyword.
2. An object is an instance of a class.
3. Attributes store data inside objects.
4. Methods define the behaviour of objects.
5. __init__() runs automatically when an object is created.
6. self refers to the current object.
7. Multiple objects can be created from one class.
8. Each object can have different attribute values.

============================================================
                    END OF NOTES
============================================================
"""
