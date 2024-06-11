
#Creating an odd numbers list from the elements of a range from 1200 to 2000 
# with steps of 125, using [List Comprehension].
oddNumbers = [n for n in range(1200,2000,125) if n % 2 != 0]
print(oddNumbers)


