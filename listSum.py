def sum(numbers:list):
    sum = 0
    for num in numbers:
        sum += num
    return sum

numbers = [2, 3, 4, 5, 15, 1, 43, 20]
total = sum(numbers)
print(f"The sum of numbers {numbers} is {total}")
