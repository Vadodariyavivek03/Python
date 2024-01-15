# Replacing

import re 

str = 'Hi, my name is vivek and i am from Rajkot, Gujrat, India.'
x = re.sub("\s", "-", str)
print(x)

y = re.sub("India.", "INDIA.", str)
print(y)
