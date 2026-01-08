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
#df_total=pd.merge(df_agg_bookings[['successful_bookings','capacity','property_id']],df_bookings[['property_id','booking_date']],on='property_id')  #here we are taking only the required columns from the tables
#print(df_total[df_total['successful_bookings']>df_total['capacity']]['booking_date'])

#data cleaning
df_bookings = df_bookings.describe()
print(df_bookings[df_bookings['no_guests']<=0])  #here we are doing the logical condition on the rows of df_bookings dataframe in the column no_guests
def converter(value):
    if int(value)<=0:
        return 0
    return value
df_bookings['no_guests'].fillna(0,inplace=True)    #here first of all we are filling the null numbers with 0 inplace the current dataframe
df_bookings['no_guests']=df_bookings['no_guests'].apply(lambda x:converter(x))  #here we are converting the column no_guests data using the function converter
print(df_bookings)

