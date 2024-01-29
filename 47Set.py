# Set : set is unordered collection data type that is iterable, immutable and has no duplicate elements.
# Set items are unchangeable, but you can remove items and add new items.

# Basic operator : 

# Accessing set value : 
# Unordered means set items can appear in a different order every time you use them, and cannot be referred to by index or key.

x = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}
print(x)

print(type(x))

# Duplicate value not allowed : 

y = {'India', 'Australia', 'UK', 'Canada', 'USA', 'India', 'Spain'}
print(y)

#-----------------------------------------------------------------------------------------------------------------------------
# len : 

x = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}
print("Length : ", len(x))

#-----------------------------------------------------------------------------------------------------------------------------
# constructor :

my_set = set(('India', 'Australia', 'UK', 'Canada', 'USA', 'Spain')) # note the double round-brackets
print("constructor : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# Union : 

set1 = {1, 2, 3}
set2 = {3, 4, 5}

uni = set1 | set2  # or set1.union(set2)
print("Union : ",uni)

#-----------------------------------------------------------------------------------------------------------------------------
# Intersection :  
# set1.intersection_update(set2) : The intersection_update() method will keep only the items that are present in both sets.

inter = set1.intersection(set2)
print("Intersection : ",inter)

#-----------------------------------------------------------------------------------------------------------------------------
# Difference : Return a new set, that contains only the elements that are NOT present in both sets.
# set1.symmetric_difference_update(set2) : This method will keep only the elements that are NOT present in both sets(output on old set).

diff = set1.symmetric_difference(set2)
print("Differnce : ",diff)

#-----------------------------------------------------------------------------------------------------------------------------
# Copy : 

x = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

y = x.copy()
print("Copy : ",y)