# Datetime function : 

import datetime

date_str = "2022-01-21 12:30:00"

x = datetime.datetime.now()

y = x.strptime(date_str, "%Y-%m-%d %H:%M:%S")

print(y)

#---------------------------------------------------------------------------------------------------------------

from datetime import datetime, timedelta

delta = timedelta(days=5)

new_date = datetime(2022, 1, 1) + delta

print(f"New Date: {new_date}")

#---------------------------------------------------------------------------------------------------------------

from datetime import datetime, timezone, timedelta

dt_with_timezone = datetime(2022, 1, 1, 12, 0, tzinfo=timezone.utc)

print(f"Datetime with Time Zone: {dt_with_timezone}")

