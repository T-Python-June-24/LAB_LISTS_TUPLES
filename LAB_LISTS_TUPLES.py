def sum_int(items:list) -> int:
    '''
    Takes a list and sums all integers in it.

    Args:
        items (list): A list of items.

    Returns:
        result (int): The sum of all integers in the list,
                      Returns None if there is a non-integer element.
    '''
    # Check that all elements in the list are integers.
    for item in items:
        # Continue looping if the element is integer.
        if type(item) == int:
            continue
        # Terminate the function when encountering a non-integer element.
        else:
            print("The list must have integer elements only.")
            return None
    result = 0
    result += item
    return result

def greatest_int(items:list) -> int:
    '''
    Takes a list and returns the greatest integer in it if any.

    Args:
        items (list): A list of items.

    Returns:
        greatest (int): The greatest integer in the list.
                        Returns None if there is a non-integer element.
    '''
        # Check that all elements in the list are integers.
    for item in items:
        # Continue looping if the element is integer.
        if type(item) == int:
            continue
        # Terminate the function when encountering a non-integer element.
        else:
            print("The list must have integer elements only.")
            return None
    greatest = items[0]
    for item in items:
         if item > greatest:
            greatest = item
    return greatest

## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
the_list:list = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter,
### and then returns  the sum  of all the items in that list.
print(sum_int(the_list))

### Q2: Write a function that takes a list as a parameter,
### and then returns the largest number from a list of numbers.
print(greatest_int(the_list))

### Q3: Create an odd numbers list from the elements of a range
### from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numbers:list = [x for x in range(1200, 2000, 125) if x % 2 != 0]
print(odd_numbers)

### Q4: use list slicing to get a new list from the previous list
### (odd numbers list) starting from the start to the 5th element in the list.
sliced_odd_numbers:list = odd_numbers[:5]
print(sliced_odd_numbers)
