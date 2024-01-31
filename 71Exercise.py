
a = [(1, 2), (2, 3)]

a.append((4, 5))
print("After adding (4, 5):", a)

a.remove((2, 3))
print("After removing (2, 3):", a)

user_input = int(input("Enter a value to filter tuples: "))
filtered_list = [tup for tup in a if user_input in tup]
print("Filtered list:", filtered_list)
