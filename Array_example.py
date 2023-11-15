# Here we will demonstrate the use of array in python

# Array is the object in the python. In order to use the array, we have to import it.

import array as ar

# Here we will allow use to generate his own array
user_arr = ar.array('i')
count = int(input("\n Please enter the number of elements you want to enter is your array :"))
for i in range(0,count):
    print("Enter ",i," element")
    inp = int(input())
    user_arr.append(inp)
print(" The array you generated is :")
print(user_arr)

