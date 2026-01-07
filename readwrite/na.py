import pandas as pd

# .fillna() is one of the most important feature of pandas DataFrame which is used to fill the N/A value with the custom data as an example
df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/final_movies.csv")
# here what we are doing is filling the null value of budget column with the mean value of whole budget column data
# and filling the null revenue data with the average of whole revenuw column data
df.fillna({
    'budget': df['budget'].mean(),
    'revenue': df['revenue'].mean()
}, inplace=True)

print(df)
df.ffill(limit=1)  #here we are filling the null value using forward fill method by limiting by 1
print(df.head(4))
#df.dropna(how='any',inplace=True)  #here if any of the column data in a row is null, that row will be dropped or deleted
df.interpolate()  #here interpolate means, pd will fill the null value using the intersection value between its next row value and prev row data
df.to_csv("C:/Users/ashok/OneDrive/Desktop/final_movies.csv", index=False)  # writing towards csv file