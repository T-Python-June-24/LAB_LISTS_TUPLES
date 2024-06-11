#Q1
list1= [2, 3, 4, 5, 15, 1, 43, 20 ]

def lists(list:list):
    number=sum(list)
    return number

print(lists(list1))

#Q2

def largest(list:list):
    for i in list:
        for j in list:
            if j > i :
                larg=j
    return larg
    
print(largest(list1))

#Q3

num = [n for n in range(1200,2000,125) if n%2==1]
print(num)


#Q4
number5=num[:5]
print(num)

