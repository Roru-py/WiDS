import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

movie = pd.read_csv("movies.csv")
rating = pd.read_csv("ratings.csv")

movie_rating = pd.merge(movie,rating, on = "movieId")
movie_rating[["movie_name","year"]]= movie_rating["title"].str.split("(",expand=True)[[0,1]]
#movie_rating['year']=movie_rating["year"].str.replace(')','')
movie_rating=movie_rating.drop(columns=["title","timestamp"])
movie_rating= movie_rating[['movieId','userId','movie_name','year','genres', 'rating']]

movies = movie_rating.pivot_table(index='userId',columns='movie_name',values='rating',fill_value=0)

user = 100
top = 10

similarity = cosine_similarity(movies)
similar = pd.DataFrame(similarity,index=movies.index,columns=movies.index)


def recommend(user,top):
    sim = similar[user].drop(user)
    weights = sim/sim.sum()

#sim_result = sim.sort_values(ascending=False).iloc[:top]
#sim1= movies[movies.index.isin(sim_result.index)].replace(0, np.nan).dropna(axis=1, how='all')

#watched = movies.loc[movies.index==user,movies.loc[user,:]>0]
    not_watched = movies.loc[movies.index!= user,movies.loc[user,:]==0]

#sim_notwatched = sim1.columns[~sim1.columns.isin(watched.columns)]
    sim_weights = pd.DataFrame(not_watched.T.dot(weights.to_numpy()),columns=["weighted_avgs"])

    return(sim_weights.sort_values(by="weighted_avgs",ascending=False).head(top))

print(recommend(user,top))

def test(user):
    watched = movies.loc[movies.index==user,movies.loc[user,:]>0]
