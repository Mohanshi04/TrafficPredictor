
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


data=pd.read_csv("traffic.csv")
data.head()


data['DateTime'] = pd.to_datetime(data['DateTime'])

# Extract and assign components of the datetime to new columns
data['Year'] = data['DateTime'].dt.year
data['Month'] = data['DateTime'].dt.month
data['DayOfMonth'] = data['DateTime'].dt.day
data['Hour'] = data['DateTime'].dt.hour
data['Minute'] = data['DateTime'].dt.minute
data['Second'] = data['DateTime'].dt.second

# Derive the day of the week and assign it to a new column
data['WeekdayName'] = data['DateTime'].dt.strftime('%A')

# Display the first few rows of the dataframe to verify the changes
data.head()
