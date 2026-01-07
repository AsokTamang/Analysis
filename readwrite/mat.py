from matplotlib import pyplot as plt
import pandas  as pd
df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/financials.csv")
df2=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fruits_data.csv")
df3=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/new_movies.csv")

fig,axes =plt.subplots(2,2)  #here we are using the graphical representation in multiple axes but in the same graphical figure
axes[0,0].plot(df['budget'],df['revenue']) #here we are passing the budget column in the x-axis and revenue column in the y-axis
axes[0,1].plot(df2['apple(1kg)'],df2['grapes(1kg)'])
axes[1,0].plot(df3['language_id'],df3['imdb_rating'])
plt.show()
