
a = [[1, 2], [2, 3]]

a.append([4, 5])
print("After adding [4, 5]:", a)

a[0].extend([6, 7])
print("After adding 6 and 7 to the first sublist:", a)

a.remove([2, 3])
print("After removing [2, 3]:", a)

a[0].remove(2)
print("After removing 2 from the first sublist:", a)

a.sort(key=lambda x: x[0])
print("After sorting based on the first element of sublists:", a)


user_input = input("Enter 'sort' to sort or 'filter' to filter: ")

if user_input.lower() == 'sort':
    sort_key = int(input("Enter the index to sort by (0 or 1): "))
    a.sort(key=lambda x: x[sort_key])
    print("After sorting based on user input:", a)

elif user_input.lower() == 'filter':
  
    filter_value = int(input("Enter the value to filter: "))
    filtered_list = [sublist for sublist in a if filter_value in sublist]
    print("Filtered list:", filtered_list)

else:
    print("Invalid input. Please enter 'sort' or 'filter'.")
