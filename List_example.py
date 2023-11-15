# Here is code excersise of List chapter from Python crash course
# Here we have to make a dynamic Guest invitation program'
# First thing is to create a complete list of Guest
# Next check whether any of them will be present or not. If not then remove them
# After having a temporary list, check the size of dinner tables.
# If there is large table then add more guest. But if no bigger table then remove the guests from the list
# Finally after all the corrections print the final list and a small invitation note for each guest

from time import sleep

def view_gustlist(glist):
    print(" Here are the list of guest :")
    for start in range(len(glist)):
        print(start," -> ",glist[start])
        sleep(1)

def invite_guest(glist):
    for ab in range(len(glist)):
        print(" Hello There!!")
        print(" I welcome ",glist[ab],' to our evening party.')
        print("Thank you very much for joing us")
        print(" ********************************************** \n")



print("                                      GUEST INVITATION PROGRAM      ")
sleep(1)
print()
print(" Our Guest list program will help you in organising and maintain a proper number of guest for your ")
print(" funtions and events. You don't have take those manual checks and all. Just let it for us ")
sleep(2)
print()
print('**********************************************************************************************************')
sleep(1)
print('**********************************************************************************************************')
sleep(1)
print('**********************************************************************************************************')
sleep(1)
print('**********************************************************************************************************')
sleep(1)
print('**********************************************************************************************************')
print('\n\n\n')
print(" Now lets prepare the inital guest list")
guest_list = []
choice = 'false'

print("How many guest are are initally planning to add ?")
count = int(input())
for cnt in range(0,count):
    print(" Please enter you Guest starting with ",cnt)
    val = input()
    guest_list.append(val)
sleep(2)

option = "false"
while option != 'true':
    print("You want to add more guest Yes/no ?  ")
    user_choice = input()
    if user_choice.lower() == "yes":
            print("Enter the name of the guest")
            val = input()
            guest_list.append(val)
    else:
            option = 'true'
            sleep(2)
print(" Your List is :")
view_gustlist(guest_list)
print("\n ************************************************************************************* \n\n")
sleep(1)
dele = 'false'

while dele.lower() != 'true':
        print("Now from above list is there any guest that might not be coming yes/no ?")
        choice = input()
        if choice.lower() == "yes":
            print("\n Please enter the name of the guest that will not be coming to event")
            name_delete = input()
            guest_list.remove(name_delete)
            view_gustlist(guest_list)
        else:
            dele = 'true'
sleep(1)
print('\n **********************************************************************************\n ')
print("\n Now Lest check with Tables arrangement!!! \n")
dele = 'false'
while dele.lower() != 'true':
    print("For the event you have all the requried tables yes / no ")
    choice = input()
    if choice.lower() == "yes":
        print(" Prefect !!!  Now we can go ahead with next step")
        print(" Here wil be final list of guest for your event : ")
        view_gustlist(guest_list)
        sleep(1)
        print("\n Shall we prepare the final phase of preparing the inviation for the guest Yes/No ?")
        choice = input()
        if choice.lower() == "yes":
            print(" Here are the inviation cards for guest :")
            invite_guest(guest_list)
            dele = 'true'
        else:
            print("\n What further actions you want to perfrom pls select that option:")
            print('1--> for adding new guest')
            print('2--> Removing any guest ')
            user_choice = int(input())
            if user_choice == 1:
                print("Please enter the name of the guest you want to add :")
                guest_name = input()
                guest_list.append(guest_name)
            if user_choice == 2:
                print(" Enter the name of guest your want to remove from list :")
                guest_name = input()
                guest_list.remove(guest_name)


