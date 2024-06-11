def getMax(numbers:list):
    max = numbers[0]
    for num in numbers:
        if max<= num:
            max = num
    return max

numbers = [2, 3, 4, 5, 15, 1, 43, 20]
max = max(numbers)
print(f"The largest number in {numbers} is {max}")
