titleIndex=0 #Position of title within the list
yearIndex=1  #Position of year within the list
rateIndex=2  #Position of rate list within the list
def anlaysisMovies(movies:list)->None:
    '''
    THIS FUNCTION ANALYSIS THE THE PROVIDED TUPLE TO GIVE AVG RATING AND DISPLYING INFO ABOUT A MOVE
    ARGS:
    MOVIE:TUPLE
    RETURN: 
    'ANLAYSED MOVIES INFO'
    '''
      #Position of rate list within the list
    anlayzedinfo=[]
    for i in range(len(movies)):
        
        if round(sum(movies[i][rateIndex])/len(movies[i][rateIndex]),2)<6.0: #calculate the avg using sum over len of rating list. and checking the  avg condition if it less than 6 then continue
            continue
        anlayzedinfo.append([movies[i][titleIndex],
                             movies[i][yearIndex],
                             round(sum(movies[i][rateIndex])/len(movies[i][rateIndex]),2)]
                             )
        


    displayMovies(anlayzedinfo) #calling a displayMovies function to display the movies info


def displayMovies(MoviesList:list)->None:
    '''
    display the anlayzed movies info in from highes rate to the lowest
    Args:
    MoivesList:int
    return:
    None
    '''
    sorted_movies = sorted(MoviesList, key=lambda x: x[rateIndex], reverse=True) # Sort the list of lists based on the rating value
    
    
    for i in range(len(sorted_movies)):
        print(f'{i+1}. {sorted_movies[i][titleIndex]} ({sorted_movies[i][yearIndex]}) - Avrage Rating: {sorted_movies[i][rateIndex]} *')
    




anlaysisMovies([
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
])
