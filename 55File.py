# File Operation : 

import json

file_path = 'Sample.txt'

list_of_dicts = []

with open(file_path, 'r') as file:
    for line in file:
        try:
            data_dict = json.loads(line)
           
            list_of_dicts.append(data_dict)

        except json.JSONDecodeError as e:
            
            print(f"Error decoding JSON on line: {line.strip()}. Error: {e}")

print(list_of_dicts)
