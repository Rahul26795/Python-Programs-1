# Following is the program that let's you make your own shopping list or to-do list
# any number of data can be added

#Date : 8-8-2020

import time

print("**************************************************************\n")
time.sleep(1)
print("                       WELOCOME TO SHOPPING LIST PROGRAM     ")
time.sleep(1)
print("")
print("\n Here we have developed a simple way to make a list quickly in efficient manner")
time.sleep(1)
print("\n************                                       ***************\n")
time.sleep(1)
print("\n************                                       ***************\n")
time.sleep(1)
print("\n************                                       ***************\n")
time.sleep(1)
print("\n************                                       ***************\n")
time.sleep(1)
print("\n************                                       ***************\n")
time.sleep(1)
print("\n************                                       ***************\n")
# now defining the functions needed
# We need to main functions -> 1 for modifying the list and other to display the finalzed list

def finalized_list(final_list):
    time.sleep(1)
    print("\n Here we will now display your final list")
    for num in range(0,len(final_list)):
        print((num + 1),"--> ",final_list[num])
        time.sleep(1)

def add_data():
    print("\n Please enter new data to be added :")
    new_data = input()
    return new_data
 

# Now we will start the main program to add the data in the list
my_list=[]     
print("\n\n  Now we will start making your list : ")
total_num = int(input(" Please enter the totat number of items you want to add :"))

for num in range(0,total_num):
    print("Enter ",num," item :")
    item = input()
    # my_list[num] =item    WRONG!!!  INCORRECT as the list is empty we cannot add.
    my_list.append(item)    # RIGHT!! Now the data will get added



# The data is added now we will have a preview
time.sleep(1)
print("\n**\n")
time.sleep(1)
print("\n**\n")
time.sleep(1)
print("\n**\n")
time.sleep(1)
print("\n**\n")
time.sleep(1)

print(" \n Following is the listt made :")
for num in range(0,len(my_list)):
    print({num+1}," -->"+my_list[num])

print("\n Do you need to change any of your data in list Yes/No")
option = input()

if option.lower() == "no" :
    finalized_list(my_list)
else:
    print("\nPlease enter from below option what you need to make the changes :")
    print("\n 1 -> Adding a new item ")
    print("\n 2 -> Deleting an item ")
    print("\n 3 -> Replace an item ")
    op = int(input())
    if op == 1:
        my_list.append(add_data())
    elif op == 2:
        print("Please enter which data is to be removed from the list :")
        remove_data = input()
        my_list.remove(remove_data)
    elif op == 3:
        print(" Please enter which number data is to be replaced")
        posi = int(input())
        new_data = input("\n Enter the new data to be added :")
        position = posi - 1
        my_list[(position)] = new_data

# Finalised List 
print("********")
time.sleep(1)
print("********")
time.sleep(1)
print("********")
time.sleep(1)
print("********")
time.sleep(1)
print("********")
time.sleep(1)
print("********")
time.sleep(1)

finalized_list(my_list)

print("********")
print("********")



