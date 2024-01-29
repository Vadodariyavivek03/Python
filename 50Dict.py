# Dictionary : key:value pairs , Items are ordered, changeable, and does not allow duplicates.

# Accessing values in dictionary :

dict = {
         'Collage' : "Darshan University",
         'City' : "Rajkot",
         'Degree' : "B.E.",
         'Branch' : "Computer Engineering",
         'Sem' : 8
       }

print(dict)
print(type(dict))

print("City :",dict.get('City'))   # or print(dict['City])

print("Keys :",dict.keys())

print("Values :",dict.values())

print("Items : ",dict.items())

print("Length : ",len(dict))

# Update dictionary : 

dict["Sem"] = 7
print("Update Dictionary : ",dict)

# or 2 : 

dict.update({'Degree' : "B.Tech."})
print("Update Dictionary : ",dict)

# Add Dictionary : 

dict["Year"] = 2024
print("Add Dictionary : ",dict)

# Delete : 

dict.pop("Year")
print("Delete : ",dict)

dict.popitem()              # removes the last inserted item.
print("Delete : ",dict)

del dict["City"]
print("Delete : ",dict)

del dict
print("Delete : ",dict)

# clear() :

x = {
         'Collage' : "Darshan University",
         'City' : "Rajkot",
         'Degree' : "B.E.",
         'Branch' : "Computer Engineering",
         'Sem' : 8
       }

x.clear()
print("Clear : ",x)