def average(numbersList:list):
    sum =0
    for num in numbersList:
        sum+=num
    average = sum / len(numbersList)   
    return round(average,2)

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

#Calculating the average of movies ratings
moviesRatings = [(title, year,average(rating)) for title, year, rating in movies if average(rating)>6]
print(moviesRatings)

#Printing the movies analysis.
i = 1
for movie in moviesRatings:
    print(f"{i}. {movie[0]} ({movie[1]}) - Avergae rating: {movie[2]} ★")
    i+=1