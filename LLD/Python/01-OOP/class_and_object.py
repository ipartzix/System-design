class Student:
    # Attributes :- variables inside the class are called attributes
    # name = ""
    # age = 0
    # gender = ""


    # methods 
    def __init__ (self):
        print("================================")
        print("this is a constructor or initilizer ")


    def set_info(self , n: str ,a : int, g:str):
        # self.name = input("Enter your Name :")
        # self.age = input("Enter your age :")
        # self.gender = input("Enter your gender :")
        self.name = n
        self.age = a
        self.gender = g
        

    def display(self):
        print(f"My name is {self.name }. age is {self.age} my gender is {self.gender} ")

# ======== Set the data =========

s1 = Student()
s1.set_info("Partha",21 , "male")
s1.display()


s2 = Student()
s2.set_info("ram", 33 ,"male")
s2.display()
