list=[2, 3, 4, 5, 15, 1, 43, 20]
#Q1 calculate the sum of the elements in the list

def list_sum(list):
 '''
 this function calculate the sum of the elements in a given list
 Args:
 list(list) : list given by user 
Return:
        sum (int): The sum of all elements in the list
'''
 sum:int=0 
 for i in list : # itrate over each item in the list 
     sum+=i
 return sum
#Q2
def largest_number(list):
     '''
     this function find the largest number in the list was given from the user 
     Args : 
      list(list) : list given by user 
      Return:
      largest_item(int) : the value of the largest item in the list 
     '''
     largest_item: int=0
     for i in list: #iterate over each number in the list
        if i>largest_item: 
           largest_item=i
     return largest_item
#Q2
list_size=int(input("Enter the number of items you want for the list : "))# take size of user's list 
user_list=[] 

#user enters the list values 

for i in range(list_size):
   item=int(input(f"Enter the {i+1} item "))
   user_list.append(item)
print("list is created")

#find the largest number in the user list by calling the largest_number function

largest_item=largest_number(user_list)
print(f"the largest item is : {largest_item}")

# call the  list_sum to count the sum for the list given in line 2
sum=list_sum(list)
print(f"the sum for the {list} list is  = {sum}")

#Q3 prints an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125
odd_numbers=[i for i in range(1200,2000,125) if i%2!=0 ]
print(odd_numbers)

# Q4 use list slicing to get a new list from the  "odd_numbers" list starting from the start to the 5th element in the list.
odd_numbers_slice=odd_numbers[:5]
print(odd_numbers_slice)