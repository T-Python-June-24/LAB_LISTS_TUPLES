# solution of bonus in lab lists and tuples 

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# calculating the average rating for each movie 

'''
for raw in range(len(movies)):
    for colunm in movies:
        print(movies[raw])

'''

for rate in movies:
        rating= sum(rate[2])/ len(rate[2])
        print(f"Movie : {rate[0]}, release year : ({rate[1]}) - Avergae rating: {round(rating,2)}")
        

#Filters out movies with an average rating lower than 6.0

#Displays the movies, along with their title, release year, and average rating.


