# File Operation : 

# Read CSV file : 

import csv

file_path = 'Book1.csv'    # file path

with open(file_path, 'r') as file:      # Open the CSV file in read mode
    csv_reader = csv.reader(file)       # Create a CSV reader object
        
    for row in csv_reader:              # Iterate through each row in the CSV file
        print(row)

#------------------------------------------------------------------------------------------------------------------------------------
# Write CSV file : 
        
import csv

file_path = 'Book2.csv'                 # file path

data_to_write = [                       # Data to be written to the CSV file.
    ['Name', 'Sem', 'Branch'],
    ['abc', 2, 'Computer'],
    ['xyz', 4, 'Civil'],
    ['pqr', 2, 'Mechanical'],
    ['stu', 8, 'Computer']
]

with open(file_path, 'w', newline='') as file:   # Sample data to be written to the CSV file
    csv_writer = csv.writer(file)                # Create a CSV writer object
    
    csv_writer.writerows(data_to_write)          # Write the data to the CSV file
    print("Success!!")
    
#------------------------------------------------------------------------------------------------------------------------------------
# Append CSV file : 
    
import csv

file_path = 'Book2.csv'                      # file path

data_to_append = ['new', 6, 'Computer Honours']    # Data to be appended to the CSV file


with open(file_path, 'a', newline='') as file:      # Open the CSV file in append mode.
    csv_writer = csv.writer(file)                   # Create a CSV writer object
    
    csv_writer.writerow(data_to_append)             # Append the data to the CSV file
    print("Success!!")