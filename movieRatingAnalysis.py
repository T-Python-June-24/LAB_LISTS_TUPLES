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

#Calculating the average of movie ratings
moviesRatings = [(title, year,average(ratings)) for title, year, ratings in movies if average(ratings)>6]

#Sorting the movies by average rating in decending order.
moviesRatings.sort(key = lambda movie:movie[2],reverse = True)

i=1
for title, year, avg_ratings in moviesRatings:
    print(f"{i}. {title} ({year}) - Avergae rating: {avg_ratings} ★")
    i+=1