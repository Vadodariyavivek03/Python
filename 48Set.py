# Set Function :

# Add item in set : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

my_set.add('New Zeland')

print("Add : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# Add item in set with update() : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

x = {'Japan', 'Greece', 'Europe'}

my_set.update(x)
print("Add with update : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# or list : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

x = ['Japan', 'Greece', 'Europe']

my_set.update(x)
print("Add with List : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# Remove item in set : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

my_set.remove('Canada')

print("Remove : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# Discard() : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

my_set.discard('Spain')

print("Discard : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# Pop() :

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

x = my_set.pop()

print("Removed item : ",x) 

print("The set after removal : ",my_set) 

#-----------------------------------------------------------------------------------------------------------------------------
# clear() : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

my_set.clear()

print("clear : ",my_set)

#-----------------------------------------------------------------------------------------------------------------------------
# del : 

set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

del set
print(set)

#-----------------------------------------------------------------------------------------------------------------------------
# Loop in set : 

my_set = {'India', 'Australia', 'UK', 'Canada', 'USA', 'Spain'}

for i in my_set:
    print("Loop : ",i)

#-----------------------------------------------------------------------------------------------------------------------------
# isdisjoint : Returns True if none of the items are present in both sets, otherwise it returns False.
    
x = {1, 2, 3}
y = {4, 5, 6}

z = x.isdisjoint(y)
print("Disjoint : ",z)

#-----------------------------------------------------------------------------------------------------------------------------
# issubset : Return True if all items in set x are present in set y.
    
x = {'a', 'b', 'c', 'd'}
y = {'f', 'e', 'c', 'a', 'd', 'b', 'g'}

z = x.issubset(y)
print("Subset : ",z)

#-----------------------------------------------------------------------------------------------------------------------------
# issuperset : Return True if all items set y are present in set x.

x = {'a', 'b', 'c', 'd'}
y = {'f', 'e', 'c', 'a', 'd', 'b', 'g'}

z = x.issuperset(y)
print("Superset : ",z)
