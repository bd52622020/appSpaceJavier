from pyspark.sql.types import Row
r_columns = ["movie_id", "movie_title", "release_date", "Video Release date",
                  "IMBd Url", "unknown", "Action", "Adventure", "Animation",
                   "Childen's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
                   "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-fi",
                   "Thriller", "War", "Western"]
ex = "235|Mars Attacks! (1996)|13-Dec-1996||http://us.imdb.com/M/title-exact?Mars%20Attacks!%20(1996)|0|1|0|0|0|1|0|0|0|0|0|0|0|0|0|1|0|1|0"
ex = ex.split("|")
genres = ex[5:]
row = {}
genres_s = ""
offset = 5
for i in range(len(genres)):
    genre_value = genres[i]
    print(i, genre_value)
    if genre_value == 1:
        genres_s = genres_s + ", " + r_columns[i+offset]
    
print(genres_s)
print
    
    






# for i in range(len(r_columns)):
#     if i != 2 and i != 3 and i != 4:
#         row[r_columns[i]] = ex[i]
        
print(row)
