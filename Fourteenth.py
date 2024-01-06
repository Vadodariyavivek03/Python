#Logical Operators  

x = int(input("Enter the number1 : "))
y = int(input("Enter the number2 : "))

#AND - It will check both value true then it's give answer true otherwise false.

if x > 0 and y > 0:
    print("TRUE")
else:
    print("FALSE")

#OR - It will check both value false then it's give answer false otherwise true.

if x > 0 or y > 0:
    print("TRUE")
else:
    print("FALSE")

#NOT - It will reverse the result, returns False if the result is true.

if not(x > 0 and y > 0):
    print("TRUE")
else:
    print("FALSE")