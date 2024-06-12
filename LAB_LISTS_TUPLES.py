#Q1
list1= [2, 3, 4, 5, 15, 1, 43, 20 ]

def lists(list:list):
    '''
    A function that displays the sum of the numbers within a list 
    
    Args:
        list (list): A list consisting of numbers
    
    '''
    number=sum(list)
    return number

print(lists(list1))

#Q2

def largest(list:list):
    '''
    A function that extracts the largest number from a list
    Args:
        list (list): the list that contains the numbers to extract the largest number
    
    '''
    for i in list:
        for j in list:
            if j > i :
                larg=j
    return larg
    
print(largest(list1))

#Q3

num = [n for n in range(1200,2000,125) if n%2==1]
print(num)


#Q4
number5=num[:5]
print(num)

