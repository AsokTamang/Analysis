import pandas as pd
df=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/movies_data.csv")
g=df.groupby('industry')
for key,data in g:
    print(key)
    print(data.size)  #the size means the total number of datas like whole datas in each group or key which is the industry currently