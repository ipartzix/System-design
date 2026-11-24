# =====================================================
#              ENCAPSULATION IN PYTHON
# =====================================================

# Definition:
# Encapsulation is one of the four main pillars of
# Object-Oriented Programming (OOP).
#
# Encapsulation means wrapping data (variables) and
# methods (functions) together inside a single class.
#
# It also helps to protect data from direct access
# and provides controlled access through methods.
#
# Real-Life Example:
# Bank Account System
#
# In a bank account, the customer should not directly
# modify the internal account balance.
#
# Instead, the customer uses methods like:
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
#
# This is an example of Encapsulation.


# =====================================================
#                  ACCESS MODIFIERS
# =====================================================

# Python commonly uses three naming conventions
# to indicate different levels of access.
#
# 1. PUBLIC ATTRIBUTE:
#
#    A public attribute can be accessed from both
#    inside and outside the class.
#
#    Example: self.name
#
#    Access: acc.name
#
#
# 2. PROTECTED ATTRIBUTE:
#
#    A single underscore (_) indicates that an
#    attribute is intended for internal use and
#    use by child classes (subclasses).
#
#    It can still be accessed from outside the class.
#
#    Example: self._balance
#
#    Access: acc._balance
#
#
# 3. PRIVATE ATTRIBUTE:
#
#    Double underscores (__) activate name mangling.
#
#    It prevents direct access using the original
#    attribute name from outside the class.
#
#    Example: self.__pin
#
#    Direct access: acc.__pin (does not access
#    the original private attribute)
#
#
# IMPORTANT:
# Python does not strictly enforce public, protected,
# and private access.
# These are mainly naming conventions, and double
# underscores provide name mangling.


# =====================================================
#                    GETTER METHOD
# =====================================================

# Definition:
# A Getter is a method used to retrieve or read
# the value of a private attribute.
#
# It allows us to access private data through
# a public method.
#
# Example:
#
# def get_balance(self):
#     return self.__balance


# =====================================================
#                    SETTER METHOD
# =====================================================

# Definition:
# A Setter is a method used to modify or update
# the value of a private attribute.
#
# It can also perform validation before changing data.
#
# Example:
#
# def set_balance(self, amount):
#     if amount >= 0:
#         self.__balance = amount
#
# This prevents invalid negative balance updates.


# =====================================================
#                    PRIVATE METHOD
# =====================================================

# Definition:
# A private method is a method whose name starts
# with double underscores (__).
#
# It is intended for internal use within the class.
#
# Example:
# def __isServerLive(self):
#     return True
#
# Python uses name mangling for private attributes
# and methods.
#
# Example:
# __balance becomes _Bank__balance internally.


# =====================================================
#                 PYTHON PROGRAM
# =====================================================


class Bank:

    def __init__(self, name: str, balance: int, pin: int):

        # PUBLIC ATTRIBUTE
        self.name: str = name

        # PROTECTED ATTRIBUTE
        self._account_type: str = "Savings"

        # PRIVATE ATTRIBUTES
        self.__balance: int = balance
        self.__pin: int = pin

    # -------------------------------------------------
    # GETTER METHOD
    # -------------------------------------------------

    def get_balance(self):
        print(f"Current Balance = {self.__balance}")

    # -------------------------------------------------
    # SETTER METHOD
    # -------------------------------------------------

    def set_balance(self, amount: int):

        if amount >= 0:
            self.__balance = amount
            print("Balance Updated Successfully")

        else:
            print("Invalid Amount")

    # -------------------------------------------------
    # PRIVATE METHOD
    # -------------------------------------------------

    def __isServerLive(self) -> bool:
        return True

    # -------------------------------------------------
    # DEPOSIT METHOD
    # -------------------------------------------------

    def deposit(self, amount: int):

        if self.__isServerLive():

            if amount > 0:
                self.__balance += amount

                print(f"Amount Deposited. " f"Current Balance = {self.__balance}")

            else:
                print("Invalid Deposit Amount")

        else:
            print("Server Down")

    # -------------------------------------------------
    # WITHDRAW METHOD
    # -------------------------------------------------

    def withdraw(self, amount: int):

        if self.__isServerLive():

            if amount <= 0:
                print("Invalid Withdrawal Amount")

            elif amount > self.__balance:
                print("Low Balance")

            else:
                self.__balance -= amount

                print(f"Amount Withdrawn. " f"Current Balance = {self.__balance}")

        else:
            print("Server Down")


# =====================================================
#                  CREATING OBJECT
# =====================================================

acc = Bank("Partha", 10000, 1234)


# =====================================================
#                 PUBLIC ACCESS
# =====================================================

# Public attributes can be accessed directly.

print(acc.name)


# =====================================================
#                PROTECTED ACCESS
# =====================================================

# Protected attributes can be accessed from outside
# the class, but this is generally discouraged.

print(acc._account_type)


# =====================================================
#                 PRIVATE ACCESS
# =====================================================

# Private attributes cannot be accessed using their
# original names from outside the class.

# print(acc.__balance)  # AttributeError

# Name mangling allows access using the mangled name,
# but this is normally not recommended.

# print(acc._Bank__balance)


# =====================================================
#                 USING GETTER AND SETTER
# =====================================================

# Check Balance using Getter
acc.get_balance()

# Update Balance using Setter
acc.set_balance(20000)

# Check Updated Balance
acc.get_balance()


# =====================================================
#                  DEPOSIT AND WITHDRAW
# =====================================================

# Deposit Money
acc.deposit(1500)

# Withdraw Money
acc.withdraw(1000)


# =====================================================
#                  IMPORTANT NOTES
# =====================================================

# 1. Public:
#    No underscore (_).
#    Example: self.name
#
# 2. Protected:
#    Single underscore (_).
#    Example: self._account_type
#
# 3. Private:
#    Double underscore (__).
#    Example: self.__balance
#
# 4. Getter:
#    Used to read private attributes.
#
# 5. Setter:
#    Used to modify private attributes.
#
# 6. Private Method:
#    Used for internal operations within a class.
#
# 7. Name Mangling:
#    Python changes the name of double-underscore
#    attributes and methods internally.
#
#    Example:
#    __balance -> _Bank__balance
#
# 8. Encapsulation:
#    Helps control access to internal data.
#
# IMPORTANT:
# Underscores do not provide complete security.
# They communicate intended access and help prevent
# accidental modification.


# =====================================================
#                     CONCLUSION
# =====================================================

# Encapsulation helps us to:
#
# 1. Protect internal data.
# 2. Control access to attributes.
# 3. Modify data using Getter and Setter methods.
# 4. Keep data and methods together in one class.
# 5. Make code more organized and maintainable.
#
# REMEMBER:
#
# ENCAPSULATION = DATA + METHODS + DATA HIDING
#
# ACCESS MODIFIERS:
#
# PUBLIC    = name
# PROTECTED = _balance
# PRIVATE   = __pin
#
# =====================================================