# Inheritance : 

# Data Hiding : 

class BaseClass:
    def __init__(self):
        self._hidden_attribute = "I am hidden"

class DerivedClass(BaseClass):
    def display_hidden_attribute(self):
        print(self._hidden_attribute)

obj = DerivedClass()            # Creating an object of the derived class
0
obj.display_hidden_attribute()  # Accessing the hidden attribute

# print(obj._hidden_attribute)  # Uncommenting this line would work but not recommended

# Method overriding : 

class BaseClass:

    def display_info(self):
        print("BaseClass method")

class DerivedClass(BaseClass):

    def display_info(self):
        print("DerivedClass method")

obj = DerivedClass()  # Creating an object of the derived class.
obj.display_info()    # Calls the overridden method in the derived class

# Method Hiding : 

class BaseClass:
    def __hidden_method(self):
        print("BaseClass hidden method")

class DerivedClass(BaseClass):
    def call_hidden_method(self):
        print()
# Creating an object of the derived class
obj = DerivedClass()
# obj.call_hidden_method()  # Uncommenting this line will raise an error



