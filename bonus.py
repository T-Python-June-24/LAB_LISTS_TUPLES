
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
#sort movies in order from 1 to 5???
#enumerate or for loop and add onw each time

for order, (title, year, ratings) in enumerate(movies, start=1):
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating >= 6.0:
        print(f"{order}. {title} ({year}) - Average Rating: {avg_rating:.2f} ★")
        