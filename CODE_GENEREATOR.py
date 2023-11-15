# Here this program with generate a random code sequence and will save it in a file.

# Later I will open the file and display all the contents present 

# from random import randint
# from time import sleep
import random
import time
print()
print("                                        Welcome                                           ")
time.sleep(1)
print("")
print("                                           TO                                             ")
print()
time.sleep(1)
print("                                MESSAGE SEQUENCE GENERATOR        ")
time.sleep(1)
print("****************************************************************************************************")
time.sleep(1)
print("****************************************************************************************************")
time.sleep(1)
print("****************************************************************************************************")
time.sleep(1)
print("****************************************************************************************************")
time.sleep(1)
print("****************************************************************************************************")
time.sleep(1)
print("****************************************************************************************************")
print()
print("Here the code messages will be generated based on numbers 0 and 1 and the msg will be a 4 digit numbers")
print("Please enter the number of code messages you want to generate")
numb = int(input())
print("\n Enter the number of bits you want per code")
wid = int(input())
text_file = open("SIGNAL_CODE.txt","a+")
for i in range(numb):
        for j in range(wid):
            n1 = str(random.randint(0,1))
            n2 = str(random.randint(0,1))
            n3 = str(random.randint(0,1))
            n4 = str(random.randint(0,1))
            #text_file.writelines(n1,n2,n3,n4)
            L = [n1,n2,n3,n4," "]
            text_file.writelines(L)
        text_file.write("\n ")
text_file.write("\n  ***********************************************  \n")
text_file.close()
print("The code is generated in the file. Please check for analysis!!!")
        
        
