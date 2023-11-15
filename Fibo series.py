#Fibo Series :

# Here the user when enters a number n, it will display fibo series n number


def fibo(n):
    f0=0
    f1=1
    for i in range(n):
        f=f0+f1
        f0=f1
        f1=f
        print(f)


print("Enter the number till generate the series that much number of times")
num=int(input())
fibo(num)
