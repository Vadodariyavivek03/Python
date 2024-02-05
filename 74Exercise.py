

a = [[1, 2], [2, 3]]

a.append([3, 4])  # Adds [3, 4] to the end of the list
a[0].append(3)    # Adds 5 to the first sublist [1, 2]

a.pop()           # Removes the last element [3, 4]
a[0].remove(2)    # Removes the element 2 from the first sublist [1, 5]

a[1][0] = 10      # Updates List.

print("Update : ",a)
