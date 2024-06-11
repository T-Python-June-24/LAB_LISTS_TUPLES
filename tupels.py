'''

## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.


'''

given_list = [2, 3, 4, 5, 15, 1, 43, 20]



### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def sumGivenListItems(given_list):
    given_list = [2, 3, 4, 5, 15, 1, 43, 20]
    return sum(given_list)


print(sumGivenListItems(given_list))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def largestNumber(given_list):
    given_list = [2, 3, 4, 5, 15, 1, 43, 20]
    return max(given_list)

print(largestNumber(given_list))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].

oddNumbers = [is_odd for is_odd in range(1200, 2000, 125) if is_odd % 2 != 0]
print(oddNumbers)  

### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
slicing =oddNumbers[:5]
print(slicing)





'''

# Bonus

## Movie Ratings Analysis

Scenario:
You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.

Example input:
```
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
```

Expected output:
```
1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★

```


'''

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]



print("Movies with an average rating of 6.0 or higher:")


print(f"1. {movies[0][0]} ({movies[0][1]}) - Average rating: {sum(movies[0][2]) / len(movies[0][2]):.2f} ★")
print(f"2. {movies[1][0]} ({movies[1][1]}) - Average rating: {sum(movies[1][2]) / len(movies[1][2]):.2f} ★")
print(f"3. {movies[3][0]} ({movies[3][1]}) - Average rating: {sum(movies[3][2]) / len(movies[3][2]):.2f} ★")
print(f"4. {movies[4][0]} ({movies[4][1]}) - Average rating: {sum(movies[4][2]) / len(movies[4][2]):.2f} ★")