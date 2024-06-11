movies=  [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

filtered=[]
for movie in movies:
    title, relsase_year, ratings = movie
    av = round(sum(ratings)/ len(ratings),2)

    if av >= 6.0:
        filtered.append((title, relsase_year, av))


i=1
for m in filtered:
    print(f"{i}. {m[0]} ({m[1]}) - Average rating: {m[2]} ★")
    i+=1

