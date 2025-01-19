import pandas as pd

# Step 1: Load the dataset
flights = pd.read_csv("flights.csv")

# Step 2: Convert ScheduledDepart and ScheduledArrival to minutes since midnight
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

flights['ScheduledDepartMinutes'] = flights['ScheduledDepart'].apply(time_to_minutes)
flights['ScheduledArrivalMinutes'] = flights['ScheduledArrival'].apply(time_to_minutes)

# Step 3: Handle cases where ScheduledArrival is earlier than ScheduledDepart
flights['ActualDuration'] = flights['ScheduledArrivalMinutes'] - flights['ScheduledDepartMinutes']
flights.loc[flights['ActualDuration'] < 0, 'ActualDuration'] += 24 * 60  # Add 24 hours for next-day arrivals

# Step 4: Check if ActualDuration equals ScheduledDuration
same_timezone_flights = flights[flights['ActualDuration'] == flights['ScheduledDuration']]

# Step 5: Count flights in the same timezone
count = same_timezone_flights.shape[0]

print(f"Number of flights in the same timezone: {count}")
