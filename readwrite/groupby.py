import pandas as pd

df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/practicefile.csv")
print(df.groupby('ProductCategory').agg(
    total_price=('Price', 'sum')))  # here we are applying aggregration method on the dataframe
# where we are grouping the data based on unique ProductCategory, and calculating the total price based on the sum of prices
grouped = df.groupby('ProductCategory')  #this provides the panda object
print(grouped['Price'].sum())  # here we are doing the same thing which is getting the total sum of the items based on category but we are not assigning the new column in the dataframe
print('The total number of items in the clothing category is:', grouped.get_group('Clothing').Quantity.sum())  #here we are retrieving the subdata of the grouped using .get_group() method
print('The total price of total number of items in electronics category is:',grouped.get_group('Electronics').Price.sum() )
print(grouped.max())   #it gets the maximum value in each numeric column data from each group
print(grouped[['Price','Quantity']].mean())  #we can pass either single column or multiple columns in a single list like here
print(f'{grouped.describe()}\n')



def grouper(index,df,col):
    if 15<=df[col].loc[index]<=20:
        return '15-20'
    elif 10<=df[col].loc[index]<15:  #here we are selecting the column name and locating the row using the passed index
        return '10-15'
    elif 5 <= df[col].loc[index] < 10:
        return '5-10'
    else:
        return '0-5'
newg=df.groupby(lambda index:grouper(index,df,'Quantity'))  #here we are grouping by the custom function by passing the current dataframe, index or the row and the column name which is quantity currently
for key,value in newg:
    print(key)
    print(value)