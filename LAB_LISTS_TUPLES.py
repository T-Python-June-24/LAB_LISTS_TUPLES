randomNumbers=[2, 3, 4, 5, 15, 1, 43, 20]
def summation(numbers:list)->int:
    '''
    a function that return the sum of a list

    Args:
    number:list
    return
    number:int
    
    '''
    return sum(randomNumbers) #output:93
print(summation(randomNumbers))
def maxmum(numbers:int)->int:
    '''
    a function return the max number in tuple
    
    args:
    number:list
    return: 
    maxNumber:int'''
    return max(randomNumbers) #Output:43

# creating odd numbers in list
oddNumbers=[x for x in range(1200,2000+1,125) if  x%2!=0] #Output:[1200, 1325, 1450, 1575, 1700, 1825, 1950]
print(oddNumbers)
#slicing odd numbers
slicedOddNumbers=oddNumbers[:5]
