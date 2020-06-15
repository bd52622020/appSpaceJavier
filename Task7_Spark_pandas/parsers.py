from datetime import datetime
from pyspark.sql.types import Row

def drop_empty_dates(line):
    row = line.split("|")
    return row[2] != ""

def parse_rating(line):
    # Get MOVIE_ID | RATING
    row = line.split()
    date = datetime.fromtimestamp(int(row[3]))
    return Row(movie_id=int(row[1]), user_id=int(row[0]), rating=float(row[2]), date_rated=date)

def parse_movie(line):
    # Get MOVIE_ID | MOVIE_TITLE | RELEASE_DATE
    row = line.split("|")
    date = datetime.strptime(row[2], "%d-%b-%Y")
    return Row(movie_id=int(row[0]), movie_title=row[1], release_date=date)

def parse_user(line):
    # Get id | age | occupation | zip code
    row = line.split("|")
    return Row(user_id=row[0], age=int(row[1]), occupation=row[3], zip_code=row[4])

def parse_movie_genres(line, columns):
    # Get MOVIE_ID | "unknown","Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"
    row = line.split("|")
    # GET RENGES IN A LIST
    genres_values, offset, list_genres = row[5:], 5, ""

    for i in range(len(genres_values)):
        genre_value = genres_values[i]
        if genre_value == "1":
            list_genres = list_genres + ", " + columns[i+offset]
            
    return Row(movie_id=int(row[0]), movie_title=row[1], genres=list_genres[2:])

def parse_movie_genres_q3(line):
    # Get MOVIE_ID | "unknown","Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"
    row = line.split("|")
    # GET RENGES IN A LIST
    return Row(movie_id=int(row[0]), movie_title=row[1], uknown=int(row[5]), action=int(row[6]), adventure=int(row[7]), animation=int(row[8]), children=int(row[9]), comedy=int(row[10]), crime=int(row[11]), documentary=int(row[12]), fantasy=int(row[13]), film_noir=int(row[14]), horror=int(row[15]), musical=int(row[16]), mystery=int(row[17]), romance=int(row[18]), sci_fi=int(row[19]), thriller=int(row[20]), war=int(row[21]), western=int(row[22]))

            
