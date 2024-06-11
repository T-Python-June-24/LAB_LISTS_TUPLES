#Getting a new list from the list [oddNumbers], 
#starting from the start to the 5th element in the list.
oddNumbers = [n for n in range(1200,2000,125) if n % 2 != 0]
print(oddNumbers)
new_list = oddNumbers[:6]
print(new_list)