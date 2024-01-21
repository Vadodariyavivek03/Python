from datetime import datetime, timedelta

# Create a timedelta object representing a duration of 5 days, 3 hours, and 30 minutes
delta = timedelta(days=5, hours=3, minutes=30)

# Use the timedelta to perform arithmetic with datetime objects
current_datetime = datetime.now()
future_datetime = current_datetime + delta
past_datetime = current_datetime - delta

print("Current datetime:", current_datetime)
print("Future datetime:", future_datetime)
print("Past datetime:", past_datetime)
