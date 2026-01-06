import pandas as pd

# df = pd.read_excel('C:/pythonprojects/start.csv.xlsx',skiprows=1)  #here this code will skip the very first row
# header helps us to assign which indexed row to be a header
# nrows helps us to retrieve the number of rows from the file
df = pd.read_excel('C:/pythonprojects/start.csv.xlsx', header=0, nrows=5,names = ['id', 'name', 'field', 'age','expyears','salary', 'state', 'enrolled']
               )  #here we are making our own custom table title
print(df)  # reading the excel file
