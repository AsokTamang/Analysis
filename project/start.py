import pandas as pd
df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_bookings.csv")
df.ratings_given.fillna(0,inplace=True)  #here the null value in ratings_given will be assigned 0 andwe must use inplace method
total_booking_platform=df.groupby('booking_platform')
#counting the total number of bookings done in each booking platform
for k,v in total_booking_platform:
    print(f'The total number of bookings done through {k} is', len(v))
    print(v)
df.head(10)