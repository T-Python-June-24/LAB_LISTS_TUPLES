given_list = [2, 3, 4, 5, 15, 1, 43, 20]

def return_sum(one):
    return sum(one)

def largest(given_list):
    return max(given_list)

odd_numbers = [num for num in range(1200, 2001, 125)]

new_list = odd_numbers[:5]

print("Sum:", return_sum(given_list))
print("Largest number:", largest(given_list))
print("Odd numbers list:", odd_numbers)
print("New list using list slicing:", new_list)
