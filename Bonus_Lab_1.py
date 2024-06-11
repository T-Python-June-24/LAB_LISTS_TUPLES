### 1. Accepts a list of movies, with each movie represented as
### a tuple containing the movie title,
### release year, and a list of user ratings.
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
    ]

### 2. Calculates the average rating for each movie.
def average_score(scores:list) -> float:
    '''
    Takes a list of integers and outputs their average

    Args:
        scores (list): List of integers.

    Returns:
        The average of the integers
    '''
    return round(sum(scores) / len(scores), 1)

### 3. Filters out movies with an average rating lower than 6.0.

def show_filter(shows:list) -> list:
    '''
    Takes a list of shows as input and outputs another list of shows
    whose average rating is greater than or equal to 6

    Args:
        shows (list): A list of shows.

    Returns:
        above_average_shows (list): A list of shows whose average rating
        is greater than or equal to 6.
    '''
    above_average_shows = list()
    for show in shows:
        average_rating = average_score(show[2])
        if average_rating >= 6:
            above_average_shows.append((show[0], show[1], average_rating))
    return above_average_shows

### 5. Displays the  movies, along with their title,
### release year, and average rating.
print(show_filter(movies))