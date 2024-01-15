# finding all words

import re

str = "Hi, my name is vivek and i am from Rajkot, Gujrat, India."

x = re.findall("am", str)
print(x)

y = re.findall('[a-n]', str)
print(y) 