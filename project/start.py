import pandas as pd
df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_bookings.csv")
df.ratings_given.fillna(0,inplace=True)  #here the null value in ratings_given will be assigned 0 andwe must use inplace method
df.head(10)