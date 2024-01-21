# Variable No. of Arguments : 

#Variable Positional Arguments (*n):

def sum(*n):
    sum = 0
    for i in n:
        sum += i
    return sum

print("Sum is :", sum(1,2,3,4,5))

#-------------------------------------------------------------------------------------------------------------------------------
#Variable Positional Arguments (**n):

def dict(**n):
    for key, value in n.items():
        print(f"{key}: {value}")

dict(Name="Vivek", Age=22, City="Australia")

