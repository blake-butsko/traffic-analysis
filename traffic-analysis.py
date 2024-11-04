import pandas as pd

# Load the data
data = pd.read_csv('traffic.csv')

# Convert DateTime column to datetime format
data['DateTime'] = pd.to_datetime(data['DateTime'])

# Extract day of the week and hour
data['DayOfWeek'] = data['DateTime'].dt.day_name()
data['Hour'] = data['DateTime'].dt.hour

# Calculate average vehicle count per day of the week and hour
quiet_times = data.groupby(['Junction', 'DayOfWeek', 'Hour']).agg({'Vehicles': 'mean'}).reset_index()

# Find the least busy hour for each junction per day
quietest_times = quiet_times.loc[quiet_times.groupby(['Junction', 'DayOfWeek'])['Vehicles'].idxmin()]

# Display results
quietest_times = quietest_times[['Junction', 'DayOfWeek', 'Hour', 'Vehicles']]
print(quietest_times)
