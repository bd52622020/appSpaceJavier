from pyspark import SparkContext, SparkConf, SQLContext
from parsers import parse_movie, parse_rating, parse_movie_genres, drop_empty_dates, parse_user, parse_movie_genres_q3
from pyspark.sql import SparkSession
from datetime import datetime

if __name__ == "__main__":
    conf = SparkConf().setAppName("queries").setMaster("local")
    sc = SparkContext(conf=conf)
    ss = SparkSession(sc)
    sq = SQLContext(sc)
    
    movies_columns = ["movie_id", "movie_title", "release_date", "Video Release date",
                  "IMBd Url", "unknown", "Action", "Adventure", "Animation",
                   "Childen's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
                   "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-fi",
                   "Thriller", "War", "Western"]
    ratings_text = sc.textFile("data/u.data")
    movies_text = sc.textFile("data/u.item")
    users_text = sc.textFile("data/u.user")
    
    # MOVIE_ID | RATING 
    ratings_rdd = ratings_text.map(parse_rating)
    # MOVIE_ID | MOVIE_TITLE | DATE(STR)
    # Clean those dates are empty and convert date
    movies_rdd = movies_text.filter(drop_empty_dates).map(parse_movie) 
    # user_id | age | occupation | zip_code
    users_rdd = users_text.map(parse_user)

    ratings = ss.createDataFrame(ratings_rdd).alias("ratings")
    movies = ss.createDataFrame(movies_rdd).alias("movies")
    users = ss.createDataFrame(users_rdd).alias("users")
    
    movies_ratings = movies.join(ratings, movies.movie_id == ratings.movie_id)
    users_ratings = users.join(ratings, users.user_id == ratings.movie_id)
    
    # Q1) Print a list of the 10 movies that received the most number of ratings. 
    q1 = ratings.groupBy("movie_id").count()
#     q1.show(10)
    
    # Q2) Print a list of the 10 movies that received the most number of ratings, 
    # sorted by the number of ratings. 
    q2 = ratings.groupBy("movie_id").count().orderBy('count', ascending=False).limit(10)
#     q2.show(10)
    
    # Q3) Print a list of the number of ratings received by each genre.
    movies_genres_rdd_3 = movies_text.map(parse_movie_genres_q3)
    movies_genres = ss.createDataFrame(movies_genres_rdd_3).alias("movies_genres")
    movies_genres_ratings = movies_genres.join(ratings, movies_genres.movie_id == ratings.movie_id)
#     movies_genres.groupBy().sum().show(10)

    # Q4) Print the oldest movie with a “5” rating.
    q4 = movies_ratings.orderBy('release_date').limit(10).filter(movies_ratings.rating == 5).limit(1)
#     q4.show(1)
    
    # Q5) Print a list of the genre of the top 10 most rated movies.
    movies_genres_rdd = movies_text.map(lambda x: parse_movie_genres(x, movies_columns))
    movies_genres = ss.createDataFrame(movies_genres_rdd).alias("movies_genres")
    q5 = movies_genres.join(q2, movies_genres.movie_id == q2.movie_id)
#     q5.show(10)
    # Q6) Print the title of the movie that was rated the most by students
    students_cutoff = users.filter(users.occupation == "student")
    most_rated_movies_students = students_cutoff.join(movies_ratings, users.user_id == movies_ratings.user_id).groupBy("movies.movie_id").count().orderBy('count', ascending=False).limit(10)
#     most_rated_movies_students.join(movies, most_rated_movies_students.movie_id == movies.movie_id).select("movie_title", "count").show(10)
    
    # Q7) Print the list of movies that received the highest number of “5” rating
    five_rating_movies = movies_ratings.filter(movies_ratings.rating == 5).groupBy("movies.movie_id").count().orderBy('count', ascending=False).limit(10)
    #five_rating_movies.join(movies, five_rating_movies.movie_id == movies.movie_id).select("movie_title", "count").show(10)
    
    # Q8) Print the list of zip codes corresponding to the highest number of users that rated movies.
    most_rating_users = users_ratings.groupBy("users.user_id").count().orderBy('count', ascending=False).limit(10)
#     most_rating_users.join(users, most_rating_users.user_id == users.user_id).select("zip_code").show(10)
    
    # Q9) Find the most rated movie by users in the age group 20 to 25.
    # Try to reduce the amount of join
    users_cutoff = users.filter((users.age >= 20) & (users.age <= 25))
    q9 = users_cutoff.join(movies_ratings, users.user_id == movies_ratings.user_id).groupBy("movies.movie_id").count().orderBy('count', ascending=False).limit(10)
    #q9.join(movies, movies.movie_id == q9.movie_id).show(10)
    
    # Q10) Print the list of movies that were rate after year 1960.
    date_cutoff = datetime(1960,1,1)
    #movies_ratings.filter(movies_ratings.date_rated > date_cutoff).show(5)
