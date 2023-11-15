#
# print("Let's find whether the number is Armstrong number or not. \n\n\n")
# print("\n Enter the number")
# num = int(input())
# num = str(num)
# num_ls = list(num)
# count = len(num_ls)
# sum = 0
# for i in range(count):
#     sum += pow(int(num_ls[i]),count)
# print(sum)
# if sum == int(num):
#     print("\n The entered number is Armstrong")

print("\n********************************************************************\n")
print("\n Lets display armstrong numbers from the given range")
first = int(input("\n Enter the first number for the range : "))
last = int(input("\n Enter the last number for the range : "))
print("\n Below are Armstrong numbers between ",first, " and ",last)
for i in range(first,last+1):
    num = str(i)
    num_l = list(num)
    count = len(num_l)
    sum = 0
    for j in range(count):
        sum += pow(int(num_l[j]),count)
    if sum == int(num):
        print(sum)
        print("")