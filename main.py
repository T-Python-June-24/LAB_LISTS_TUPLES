# Question one solution
my_list = [2, 3, 4, 5, 15, 1, 43, 20]

def list_sum(list):
  total = 0
  for i in range(0, len(list)):
    total = total + list[i]
  print("Sum of all elements in given list: ", total)

list_sum(my_list)

# Question 2 solution
def largest_num(list):
  print("The largest number is: ",max(list))

largest_num(my_list)


# Question 3 solution
numbers_list = range(1200, 2000, 125)
odd_number_list = [ num for num in numbers_list if num % 2 != 0]  
print("The list of odd numbers is: ",odd_number_list) 

# Question 4 solution
sliced_list = odd_number_list[:5]
print(sliced_list)