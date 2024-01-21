# Datetime function : 

import datetime

date_str = "2022-01-21 12:30:00"

x = datetime.datetime.now()

y = x.strptime(date_str, "%Y-%m-%d %H:%M:%S")

print(y)

#---------------------------------------------------------------------------------------------------------------


