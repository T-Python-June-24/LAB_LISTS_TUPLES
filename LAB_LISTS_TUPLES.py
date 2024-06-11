def sum_int(items:list) -> int:
    '''
    Takes a list and sums all integers in it.

    Args:
        items (list): A list of items.

    Returns:
        result (int): The sum of all integers in the list,
                      Returns 0 if no integers were found.
    '''

    result = 0
    for item in items:
        # Check if the current item is an integer
        if type(item) == int:
            result += item
    return result

def greatest_int(items:list) -> int:
    '''
    Takes a list and returns the greatest integer in it if any.

    Args:
        items (list): A list of items.

    Returns:
        greatest (int): The greatest integer in the list.
                        Returns 0 if no integers were found.
    '''
    greatest = 0
    for item in items:
        if type(item) == int:
            if item > greatest:
                greatest = item
    return greatest

print(sum_int([2, 3, 4, 5, 15, 1, 43, 20]))
print(greatest_int([2, 3, 4, 5, 15, 1, 43, 20]))
odd_numbers:list = [x for x in range(1200, 2000, 125)]
print(odd_numbers)
sliced_odd_numbers:list = odd_numbers[:6]
print(sliced_odd_numbers)
