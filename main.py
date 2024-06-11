list = [2, 3, 4, 5, 15, 1, 43, 20]

def sum_list(list):
    return sum(list)

print(sum_list(list))

def largest_value(list):
    return max(list)

print(largest_value(list))

odd_numbers = [number for number in range(1200, 2001, 125) if number % 2 != 0]

odd_numbers_from_5 = odd_numbers[:5]

print(odd_numbers)
print(odd_numbers_from_5)
