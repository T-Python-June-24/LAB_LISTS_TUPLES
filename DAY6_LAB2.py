# LAB_LISTS_TUPLES


## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
# Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.



###1

list1 = [2, 3, 4, 5, 15, 1, 43, 20]

def func1(x:list):
    list_sum = sum(list1)
    return list_sum

print("\n#1")
print(f"Sum of numbers in the list is:\t {func1(list1)}")



###2

def func2(x:list):
    largest_number = max(list1)
    return largest_number

print("\n#2")
print(f'Largest # in the list is:\t {func2(list1)}')



###3

odd_numbers = []

for x in range(1200, 2000, 125):
    if x %2 != 0:
        odd_numbers.append(x)

print("\n#3")
print(odd_numbers)



###4

new_list = odd_numbers[:5]

print("\n#4")
print(new_list)
