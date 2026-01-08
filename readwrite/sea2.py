import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_excel("C:/Users/ashok/OneDrive/Desktop/scatter_plot.xlsx")
print(df.describe())
print(df.head(5))
sns.scatterplot(data=df,x='area_square_ft',y='price')  #using scatterplot api
plt.show()