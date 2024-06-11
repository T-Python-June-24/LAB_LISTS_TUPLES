list1 = [2, 3, 4, 5, 15, 1, 43, 20]

def sumL (x:list):
    print("The sum of the given list is ",sum(list1))

sumL(list1)

'''That was the Sum of the list numbers'''

def largestNo (y:list):
    largest = y[0]
    for i in y:
        if i>largest:
            largest = i
    print("The largest number in the list is ",largest)

largestNo(list1)

'''that was the largest number in the list'''

z=[]
def OddNo (z):
    for i in range(120,2000,125):
        if i%2 == 1:
            z.append(i)
    print("The desired Odd Numbers list is ",z)
    #print("The sliced list is ",z[0:5])

OddNo(z)

'''That was a list of odd numbers with steps of 125 within a range'''

SlicedL = z[0:5]
print(SlicedL)

'''That was a sliced list'''