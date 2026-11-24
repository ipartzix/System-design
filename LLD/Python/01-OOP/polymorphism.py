class UPI:
    def payment(self):
        print("Payment done using UPI")


class CreditCard:
    def payment(self):
        print("Payment done using Credit Card")


class Cash:
    def payment(self):
        print("Payment done using Cash")


# Creating objects
p1 = UPI()
p2 = CreditCard()
p3 = Cash()

# Calling the same method
p1.payment()
p2.payment()
p3.payment()


# POLYMORPHISM IN PYTHON
#
# Definition:
# Polymorphism is one of the four main pillars of
# Object-Oriented Programming (OOP).
# The word Polymorphism means "One Name, Many Forms".
#
# It allows the same method or function to perform
# different tasks depending on the object.
#
# Real-Life Example:
# Payment System
#
# In real life, we can make payments using different
# methods such as UPI, Credit Card, and Cash.
# The purpose of all three methods is the same,
# which is to make a payment, but the way they work
# is different.
#
# Python Program:


class UPI:
    def payment(self):
        print("Payment done using UPI")


class CreditCard:
    def payment(self):
        print("Payment done using Credit Card")


class Cash:
    def payment(self):
        print("Payment done using Cash")


# Creating objects
p1 = UPI()
p2 = CreditCard()
p3 = Cash()


# Calling the same method using different objects
p1.payment()
p2.payment()
p3.payment()


# Output:
# Payment done using UPI
# Payment done using Credit Card
# Payment done using Cash


# Explanation:
# 1. We create three classes: UPI, CreditCard, and Cash.
# 2. Each class contains the same method named payment().
# 3. Each payment() method performs a different action.
# 4. We create three objects: p1, p2, and p3.
# 5. We call the same method using all three objects.
# 6. Each object produces a different output.
#
# Conclusion:
# This is called Polymorphism because the same method
# name behaves differently for different objects.
#
# Remember:
# One Method + Different Objects + Different Behaviour
# = POLYMORPHISM
