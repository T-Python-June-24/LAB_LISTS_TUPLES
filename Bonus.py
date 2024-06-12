
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
def average_rating(movies):
    '''
    calculate the avrage rate and displays movies with rate equal or above 6.0
    Args: 
    movie(tupel):tuple with movie title , year, rating 

    '''
    i=0
    for movie in movies: # iterate over each movie in the movies tuple
        
        title, year, ratings = movie
        avg_rating = sum(ratings) / len(ratings)
        
        if avg_rating >= 6.0:
           i=i+1
           print(f"{i}- {title} ({year}) - Average rating: {avg_rating:.2f} ★")
           
average_rating(movies)