# Access Specifier : 

# Public : 

class Public:
    def __init__(self, value):
        self.value = value  # Public attribute

    def display(self):
        print(self.value)  # Public method 

obj = Public(10)
obj.display()

# Protected : 

class Protected:

    def __init__(self, value):
        self._value = value  # Protected attribute

    def _display(self):
        print(self._value)  # Protected method

class SubClass(Protected):
    def show(self):
        self._display()  # Accessing protec)ted method from subclass

obj = SubClass(20)
obj.show()

# Private : 

class Private:

    def __init__(self, value):
        self.__value = value  # Private attribute

    def __display(self):
        print(self.__value)  # Private method

obj = Private(30)

# Accessing private attribute and method directly will result in an error
# obj.__display()  # Uncommenting this line will raise an error
# print(obj.__value)  # Uncommenting this line will raise an error



