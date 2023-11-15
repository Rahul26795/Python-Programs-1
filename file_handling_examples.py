# full FILE I/O operation demonstration


file = open('my_test_file.txt','w')   #  Here we are creating a new file in the dir
L =['Hello Everyone','\nWe will be learning new methods for file handing in python\n','I need push more\n','Python is awesome\n']

file.write("I am learning to code in python \n")

file.writelines(L)
file.close()

###########################################

file = open('my_test_file.txt','r')
print(file.read())   # read method will print all the data instead the file

#  file.readlines()  <--  This method will print one line at a time.
###############################################

#  file.seek(n)  <----   The seek method will take file handle to nth  byte from start

file.seek(0)
print('\nThe output of the file.read(5) :')
file.read(5)
print()


file.seek(0)
print('\n The output of the code file.readline(5) :')
file.readline(5)
print()

file.seek(0)
print('\nThe output of the file.readlines is :')
file.readlines()
file.close()
print('\n\n *************************************\n')

