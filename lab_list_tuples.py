lst = [2,3,4] # create a list to use it in each function 

# start q1 

def list_sum (ls:list): # void function print the sum of a given array 
    '''
        the function takes a list of number and return a sum of elemnts in that list 
    '''
    sum = 0 
    for i in ls :
        sum += i
    return sum

sum = list_sum(lst) 
print(f" Q1 the sum of list {lst} is = {sum} ")


# start q2 

def largest_number (ls:list): # void function print the sum of a given array 
    '''
        the function takes a list of number and return a largest number of elemnts in that list 
    '''
    largest_num = lst[0] # assume that the first element is the largest and compeare it with another elements 
    
    for i in ls :
        if largest_num < i:
            largest_num = i 
        
    return largest_num

largest_num = largest_number(lst)
print(f" Q2 the largest number in list {lst} is = {largest_num}")


# start q3 

def generate_odd_number_list()-> list: # return a list 
    
    '''
        the function create a list 
        that contain only odd numbers in range 1200 - 2000 for every 125 steps
    '''
    odd_numbers = []
    for i in range(1200,2001,125):
            if i % 2 != 0:
                odd_numbers.append(i)
    return odd_numbers  # another solution 


generated_odd_list = [i for i in range(1200,2001,125) if i % 2 != 0]

print(f" Q3 the odd numbers in list from 1200 to 2000 with 125 steps is = {generated_odd_list}")

# start q4 

list_after_slicing = generated_odd_list[:5] # list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.

print(f" Q4 the new list after list slicing from the odd numbers list {generated_odd_list} is = {list_after_slicing}")
