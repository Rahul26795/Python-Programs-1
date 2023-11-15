# Following is the program that will calculate the factorial of the givem input number

def factorial(num):
    #fact = 1
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
        #fact1 = fact
        #fact = num
    return fact   

print("")
print("")
print(" Hello, Please enter your number whose factorial is to be calculated :") 
number = int(input())
factor = factorial(number)
print("\n The factorial of given  number is : ",factor)       
print("")
