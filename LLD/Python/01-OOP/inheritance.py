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