import pandas as pd
import numpy as np



yt = pd.read_csv("2018_Yellow_Taxi_Trip_Data.csv")

# Question 1
df_q1 = yt[['passenger_count', 'trip_distance']]
df_q1 = df_q1[df_q1['passenger_count'] <= 2]
average_distance = df_q1['trip_distance'].mean()

# Question 2
dt1 = pd.to_datetime(yt.tpep_pickup_datetime)
dt2 = pd.to_datetime(yt.tpep_dropoff_datetime)
df_q2 = pd.concat([dt1,
                   dt2,
                   dt1.dt.day_name(),
                   dt2 - dt1],
                  axis=1)
df_q2.columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'weekday', 'trip_time']

df_q2 = df_q2[(df_q2['weekday'] == 'Saturday') | (df_q2['weekday'] == 'Sunday')]

saturday_mean = df_q2[(df_q2['weekday'] == 'Saturday')]['trip_time'].mean()
sunday_mean = df_q2[(df_q2['weekday'] == 'Sunday')]['trip_time'].mean()

satur_sun_days_mean = df_q2['trip_time'].mean()

# Question 3
