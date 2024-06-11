## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
list = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def sum(list:[]):
    sum=0
    for i in list:
        sum+= i
    return sum

print(f"The sum of the list is {sum(list)}")

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def max(list:[]):
    temp=0
    for i in list:
        if i > temp:
            temp = i
    return temp

print(f"The largest number of the list is {max(list)}")

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
nums = range(1200,2000,125)
odd_nums = [num for num in nums if num % 2 != 0]
print(odd_nums)

### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
five_odds= odd_nums[:5]
print(five_odds)