import pandas as pd

df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fruits_data.csv")
print(df.shape)  # 10 number of rows and 6 columns
print(df.columns)  # printing all the columns
new_df = df.fillna({
    'apple(1kg)': df['apple(1kg)'].mean(),
    'banana(1 dozen)': df['banana(1 dozen)'].mean(),
    'grapes(1kg)': df['grapes(1kg)'].median(),
    'mango(1kg)': df['mango(1kg)'].median(),
    'Water Melons(1)': 'Not Available',
})
print(df.ffill())
print(df)
print(new_df)
