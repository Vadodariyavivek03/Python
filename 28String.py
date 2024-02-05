  # Ignore Case regular expression.

import re

pattern = re.compile(r'india', re.IGNORECASE)

str = "Hi, my name is vivek and i am from Rajkot, Gujrat, India."

match = pattern.search(str)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
