
a = [{'a1': 1, 'b1': 2}, {'a2': 2, 'b2': 1}]

a.append({'c1': 3, 'd1': 4})
print("After adding {'c1': 3, 'd1': 4}:", a)

a[0]['e1'] = 5
print("After adding ('e1', 5) to the first dictionary:", a)

a.remove({'a2': 2, 'b2': 1})
print("After removing {'a2': 2, 'b2': 1}:", a)

if 'b1' in a[0]: 
    del a[0]['b1']
print("After removing 'b1' from the first dictionary:", a)

key_to_filter = input("Enter the key to filter: ")
filtered_dicts_by_key = [d for d in a if key_to_filter in d]
print(f"Filtered list of dictionaries by key '{key_to_filter}':", filtered_dicts_by_key)

value_to_filter = int(input("Enter the value to filter: "))
filtered_dicts_by_value = [d for d in a if any(value_to_filter == v for v in d.values())]
print(f"Filtered list of dictionaries by value '{value_to_filter}':", filtered_dicts_by_value)
