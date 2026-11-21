class Student:
    # Attributes :- variables inside the class are called attributes
    name = ""
    age = 0
    gender = ""

    def set_info(self):
        self.name = input("Enter your Name :")
        self.age = input("Enter your age :")
        self.gender = input("Enter your gender :")


    def display(self):
        print(f"My name is {self.name }. age is {self.age} my gender is {self.gender} ")

# ======== Set the data =========

s1 = Student()
s1.set_info()
s1.display()


s2 = Student()
s2.set_info()
s2.display()
