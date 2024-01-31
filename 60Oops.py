# Function : 

class Dog():
    
    def __init__(self, name, age):      # Constructor method to initialize attributes
        self.name = name
        self.age = age

    def display_info(self):              # Instance method to display information about the dog
        print(f"Name: {self.name}, Age: {self.age}")

    def bark(self):                      # Instance method to make the dog bark
        print("Woof! Woof!")

dog1 = Dog("Buddy", 3)                   # Instance method to make the dog bark
dog2 = Dog("Max", 5)


dog1.display_info()                      # Accessing attributes and calling methods of objects
dog2.display_info()  

dog1.bark() 
dog2.bark() 
