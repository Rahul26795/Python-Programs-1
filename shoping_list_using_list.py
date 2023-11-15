# Here we will use append funtion to add new items/data in empty list

import time

my_list =[]
print("\n Enter the total number of items to be added in list starting with 0. Example from 0 to 9 total = 10")
total =int(input())
time.sleep(1)
print("\n **************************************************\n")
time.sleep(1)
print("Now we will enter the items you want in list :")
print("\n\n ************************************************* \n\n")
for num in range(0,total):
     print(" Please enter the ",num," item of the list")
     item = input()
     my_list.append(item)
     print("\n")

print(" Now we will display the list of items you want to entered")
for num in range(len(my_list)):
     print(num," -----> " + my_list[num])
     print("\n")
     time.sleep(1)

time.sleep(2)
print(" Thank you for using the shoping list program")
time.sleep(1)
print("\n *************************************************\n")

#  The next further the program can be extended is to add two functions. One will help modify the list. After adding all the items, it should give you an option
# to preview the and once you have confirmed all the changes, you will get to see the final list.
