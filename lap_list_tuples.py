def my_list (list):
    return sum(list)
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
print(sum(my_list))

def largest_number(list):
    return max(list)
print(max(my_list))  

odd_numbers=[i for i in range(1200,2000,125) if i%2!=0 ]
print(odd_numbers)
new_numbers=odd_numbers[:5]
print(odd_numbers)

#Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
##Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
#Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.



#bonus
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

for i, movie in enumerate(movies):
    average_rating = sum(movie[2])/len(movie[2])
    print(f"{i+1}. {movie[0]} ({movie[1]}) - Average rating: {average_rating:.2f} *")