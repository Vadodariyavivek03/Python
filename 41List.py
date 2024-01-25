# List function :

# append() : this method will add element at the end of the list.

list = ['rajkot', 'surat','ahmedabad', 'morbi', 'rajkot']

list.append('amreli')
print("append : ",list)

# extend() : this method will add one data structure (List or any) to current list.

list1 = ['kutch','porbandar', 'baroda']

list.extend(list1)
print("extend : ",list)

# insert() : this method will add element at the specified index in the list.

list.insert(0, 'Gujrat')
list.insert(2, 'dwarka')
print("insert : ",list)

# remove() : this method will remove first occurrence of specified element.

list.remove('Gujrat')
print("remove : ",list)

# index() : this method will return first index of the specified element.

str = list.index('kutch')
print("index : ",str)

# count() : this method will return the number of occurrence of the specified element.

str = list.count('rajkot')
print("count : ",str)

# sort() : this method will sort the elements in the List.

list.sort()
print("sort : ",list)

list.sort(reverse=True)
print("Reverse sort : ",list) 

# reverse() : this method will reverse the elements of the List.

list.reverse()
print("Reverse list : ",list) 

