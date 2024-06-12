# Q1 ---------------------------------------------
def sumOfNumbers (list: int) -> int: 
    '''This function is for returns  the sum  of numbers'''
    if not list:
        return print("List is empty")
    return sum(list)

# Q2 ---------------------------------------------
def largestNumber (list: int) -> int:
    ''' This function is for return largest number'''
    if not list:
        return print("There is no list")
    return max(list)



ListOfnumber = [2, 3, 4, 5, 15, 1, 43, 20]

print(sumOfNumbers(ListOfnumber))
print(largestNumber(ListOfnumber))

# Q3 ---------------------------------------------

numbers = [i for i in  range(1200, 2000, 125)]
# Use list comprehension to filter out odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)
# Q4 ---------------------------------------------

new_list = numbers[:5]
print (new_list)

