# Constructor : 

class Jupical:

	def __init__(self):         # default constructor
		self.Jupi = "Jupical Technologies Pvt. Ltd."

	def print_Jupi(self):       # a method for printing data members
		print(self.Jupi)

obj = Jupical()

obj.print_Jupi()                # calling the instance method using the object obj.

# Parameterized Constructor :
class Addition:
	first = 0
	second = 0
	answer = 0

	def __init__(self, f, s):       # Parameterized Constructor
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

obj1 = Addition(1000, 2000)             # creating object of the class
                                        # this will invoke parameterized constructor
obj2 = Addition(10, 20)                 # creating second object of same class

obj1.calculate()                        # perform Addition on obj1

obj2.calculate()                        # perform Addition on obj2

obj1.display()

obj2.display()


