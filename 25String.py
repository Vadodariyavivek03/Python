# Regular expression 

import re 

str ='Hi, my name is vivek and i am from Rajkot, Gujrat, India.'

x = re.search("^Hi.*India.$",str)

if x : 
    print("Something is exist.")
else : 
    print("Not exists.")

  
