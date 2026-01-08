import pandas as pd
df_agg_bookings = pd.read_csv('C:/Users/ashok/OneDrive/Desktop/fact_aggregated_bookings.csv')
df_bookings = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_bookings.csv")
df_date=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_date.csv")
df_hotel=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_hotels.csv")
df_room=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_rooms.csv")
maximum = df_agg_bookings.capacity.max()

print(maximum)
print(df_agg_bookings[df_agg_bookings['capacity']==maximum]['property_id'])  #here we are selecting the property id having the maximum capacity
print(df_bookings.shape)
df_total=pd.merge(df_agg_bookings[['successful_bookings','capacity','property_id']],df_bookings[['property_id','booking_date']],on='property_id')  #here we are taking only the required columns from the tables
print(df_total[df_total['successful_bookings']>df_total['capacity']]['booking_date'])