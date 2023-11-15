# DATE 22-05-2020 

#Here we will use file processing functions in ordeer to open read and write on the file.

# open()  --> open function is to open a file. While using this function we need to assign an object to it.
# read()  --> Read function is used to read the contents of the file. 
# readline() --> Readline function is used to read first line of the text. we can pass the number or the position
# of the line to read
# close() -->  Close function is used to close the file after it's use. It should be done so that there will no
#    buffer issues with the open file

#  Demo_text.txt is created.

text_file = open("Demo_text.txt","r")
print(text_file.read())                     # Displaying all the details 
text_file.close()

#Now we willread and display certain number of lines
# print()
# text = open("Demo_text.txt","r")
# print(text.readline())

# print(text.readline())

# print(text.readline())

# print(text.readline())
# text.close()
print("************************************************")

# Now we will enter some data in the file. For this we will be using the write function
L = ["\n HI There !!! \n","This is write function used to write a string into a file \n","We are learning file processing",
"After that we will continue with the course"]
text = open("Demo_text.txt","w+")            # opening with read and write mode
text.write("WELCOME TO PYTHON \n")
print()
print("After writing the string here is the output :")
print()
print(text.read())

print("\n Now after entering the string list. here is the second output :")
#text.write(L)
text.writelines(L)
print(text.read())

text.close()