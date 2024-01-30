# File Operation : 

# Read from Excel file : 

import pandas as pd

fp = 'Example1.xlsx'

dataframe1 = pd.read_excel(fp)

print(dataframe1)

#------------------------------------------------------------------------------------------------------------------------------------
# Write Excel file : 
        
import pandas as pd

fp = 'Example2.xlsx'

data_to_write = {'Name': ['John', 'Alice', 'Bob'],
                 'Age': [25, 30, 22],
                 'City': ['New York', 'San Francisco', 'Chicago'],
                 'Country': ['USA', 'California', 'US'],
                 'Gender': ['Male', 'Female', 'Male']}

df_to_write = pd.DataFrame(data_to_write)

df_to_write.to_excel(fp, index=False)

    
#------------------------------------------------------------------------------------------------------------------------------------
# Append Excel file : 
    
import pandas as pd

fp = 'Example2.xlsx'

data_to_append = {'Name': ['Eve'],
                  'Age': [28],
                  'City': ['Los Angeles'],
                  'Country': ['California'],
                  'Gender': ['Male']}

df_to_append = pd.DataFrame(data_to_append)

df_existing = pd.read_excel(fp)

df_updated = pd.concat([df_existing, df_to_append], ignore_index=True)

df_updated.to_excel(fp, index=False)
           
    