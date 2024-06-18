movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

x = [(m[0], m[1], m[2]) for m in movies if (sum(m[2])/len(m[2])) >= 6]
x.sort()
x.reverse()

for m in x:
    print(f"{m[0]} ({m[1]}), {round(sum(m[2])/len(m[2]),2)}*")