# Exception Handling : 

# Try : test a block of code for errors.

x = 2
y = 'Hi'

try:
    z = x + y
    print(z)

except TypeError:
    print("Error : Can't add int and str.")

#-----------------------------------------------------------------------------------------------------------------------------
# Exception : block lets you handle the error.
    
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero!")

except:
    print("An error occurred!")

#-----------------------------------------------------------------------------------------------------------------------------
# Pass : No-operation statement. It is used when a statement is syntactically required but you want to do nothing or have an empty block.
    
try:
    result = 10 / 0
    
except ZeroDivisionError:
    print("Cannot divide by zero!")
    pass

except:
    print("An error occurred!")

#-----------------------------------------------------------------------------------------------------------------------------
# Else : this keyword to define a block of code to be executed if no errors were raised.
    
try:
  print("Hello")

except:
  print("Something went wrong")

else:
  print("Nothing went wrong")

#-----------------------------------------------------------------------------------------------------------------------------
# Finally : this block, if specified, will be executed regardless if the try block raises an error or not.
  
try:
  print(x)

except:
  print("Something went wrong")
  
finally:
  print("The 'try except' is finished")