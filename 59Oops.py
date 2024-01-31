# Instance and Static : 

# Instance methods 

class shape(): 
	
	def __init__(self, edge, color): 
		self.edge = edge 
		self.color = color 
		
	def finEdges(self):                 # Instance Method 
		return self.edge 
	
	def modifyEdges(self, newedge):     # Instance Method 
		self.edge = newedge 
		
circle = shape(0, 'red')                # Driver Code 
square = shape(4, 'blue') 

print("No. of edges for circle: "+ str(circle.finEdges()))   # Calling Instance Method 

square.modifyEdges(6)       # Calling Instance Method 

print("No. of edges for square: "+ str(square.finEdges())) 

# Static Method : 
 
class Calculate():

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

add = Calculate.add(3, 5)				# Calling static methods without creating an instance
multiply = Calculate.multiply(4, 6)

print("Sum : ",add)       
print("Multiply : ",multiply)  



