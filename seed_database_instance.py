from create_database_instance import db, insert_movie, create_table
import pandas as pd
import sqlite3



# while __name__ == "__main__":
db.call_db(create_table)
data = pd.read_csv("Movies_final_1.csv")
df = pd.DataFrame(data)
df.drop(columns="Unnamed: 0", inplace=True)
# for movie in df.iterrows():
#     mov = movie[1]
#     # print(mov["Title"])

#     db.call_db(insert_movie, mov["Rank"], mov["Title"], mov["Lifetime_Gross"], mov["Year"], mov["Movie_id"], mov["Image"], mov["Director"])

#     # data.to_sql("Movies", sqlite3.connect(db.url), if_exists='append', index=False)


for num, movie in df.iterrows():
    rank = movie["Rank"]
    title = movie["Title"]
    lifetimegross = movie["Lifetime_Gross"]
    year = movie["Year"]
    movie_id = movie["Movie_id"]
    image = movie["Image"]
    director = movie["Director"]
    db.call_db(insert_movie, rank, title, lifetimegross, year, movie_id, image, director)