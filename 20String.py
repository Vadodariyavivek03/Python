# Create Substring -- Using string slicing, we can specify start index, end index and steps (colon separated) to slice the string.
#subx = x[start index:end index:steps] 

x = "Hi, my name is vivek and i am from Rajkot, Gujrat, India."

sub1 = x[0:8]
print(sub1)

sub2 = x[5:24]
print(sub2)

sub3 = x[16::3]
print(sub3)

sub4 = x[:5:2]
print(sub4)

sub5 = x[::-1]
print(sub5)

sub6 = x[::2]
print(sub6)