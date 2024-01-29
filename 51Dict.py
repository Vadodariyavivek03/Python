# Dictionary function : 

# Copy() : 

dict = {
         'Collage' : "Darshan University",
         'City' : "Rajkot",
         'Degree' : "B.E.",
         'Branch' : "Computer Engineering",
         'Sem' : 8
       }

x = dict.copy()
print("Copy : ",x)

# fromkeys() : 

x = {
      'Collage' : "Darshan University",
      'City' : "Rajkot",
      'Degree' : "B.E.",
      'Branch' : "Computer Engineering",
      'Sem' : 8
    }

y = dict.fromkeys(x)    #  y = 0 --> dict.fromkeys(x,y) ---> It will print value is 0 every keys.

print("Fromkeys : ",y)

# has_key() :

# print(x.has_key('City')) ---> python 3 removed this function instead of use 'in operator' :

x = {
      'Collage' : "Darshan University",
      'City' : "Rajkot",
      'Degree' : "B.E.",
      'Branch' : "Computer Engineering",
      'Sem' : 8
    }

print("x : {}".format(x))

if 'City' in x:
    print(x['City'])
else:
    print("{} is Absent".format('City'))

if 'Year' in x.keys():
    print(x['Year'])
else:
    print("{} is Absent".format('Year'))

# set default() : Returns the value of the item with the specified key.

y = x.setdefault('Degree',"B.E.")
print("Set-Default : ",y)

# cmp() : 

dict1 = {
         'Collage' : "Darshan University",
         'City' : "Rajkot",
         'Degree' : "B.E.",
         'Branch' : "Computer Engineering",
         'Sem' : 8
       }

dict2 = {
         'Collage' : "Darshan University",
         'City' : "Rajkot",
         'Degree' : "B.E.",
         'Branch' : "Computer Engineering",
         'Sem' : 8
       }

# x = cmp(dict1,dict2)  ----> Python 2 function.......
# print(x)
# python 3 :

if dict1 == dict2:
    print("Equals Dictionary.")


# str : 

print(str(x))


