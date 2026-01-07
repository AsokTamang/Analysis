import pandas as pd
df_movies = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/movies.csv")
df_languages=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/languages.csv")
df_financials=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/financials.csv")
df_newmovies=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/new_movies.csv")
df_movies = pd.concat([df_movies,df_newmovies],ignore_index=True)
df_movies.tail(5)  #only showing the last 5 datas using .tail
df_movies = pd.merge(df_movies,df_languages,on="language_id",how="inner")  #merging the two dfs using the inner join method
df_movies=pd.merge(df_movies,df_financials,on="movie_id",how="left") #here we are using left join
newData=df_movies[['movie_id','title','lang_name','budget','revenue','currency']]
newData.to_csv("C:/Users/ashok/OneDrive/Desktop/final_complete_data.csv",index=False)  #here we are removing the index data
print(newData.head(3).revenue.max())