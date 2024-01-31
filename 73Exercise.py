
a = [[{'a1': 1, 'b1': 2}], [{'a2': 2, 'b2': 1}]]

new_dict1 = {'c1': 3, 'd1': 4}
a[0].append(new_dict1)

new_dict2 = {'c2': 4, 'd2': 3}
a[1].append(new_dict2)

removed_dict1 = a[0].pop(0)

removed_dict2 = a[1].pop(1)

print("After Removing :")
print(a)
