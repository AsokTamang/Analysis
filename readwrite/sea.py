import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_excel("C:/Users/ashok/OneDrive/Desktop/histograms.xlsx")
sns.histplot(df['Exam_Score'],kde=True)  #here we are using the Blood_Sugar column inorder to build the histogram
print(df.head())
plt.show()
