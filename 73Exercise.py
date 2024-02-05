
a = [[{'a1': 1, 'b1': 2}], [{'a2': 2, 'b2': 1}]]

# new_dict1 = {'c1': 3, 'd1': 4}
# a[0].append(new_dict1)

# new_dict2 = {'c2': 4, 'd2': 3}
# a[1].append(new_dict2)

# removed_dict1 = a[0].pop(0)

# removed_dict2 = a[1].pop(1)

# print("After Removing :")
# print(a)


dict1 = {"c1":5, "d1":3}
a[1].append(dict1)
print(a)

dict2 = {'d1':56, 'c2':32}
a[0].append(dict2)
print(a)

a[1].pop(0)
print(a)

a[0][1] = 25
print("Update : ",a)