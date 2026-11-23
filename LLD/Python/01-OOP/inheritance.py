class Animal: # parent
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Dog(Animal): #child
    def bark(self):
        print("I am barking")


dog = Dog()

dog.bark()
dog.eat()
dog.sleep()

animal = Animal()
animal.sleep()
animal.eat()