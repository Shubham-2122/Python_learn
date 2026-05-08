'''
File : File Data Entery you can enter and reomve session
Enerty log Use karva
File Method Are there in 3 W,R,A    
'''
# W : Write Mode
file = open("test.txt","w")
file.write("This is File Management demo using python")
file.close()
print("File written Successfully")
print("*********************************************")

#R : Read Mode
# file nahi hoy to read thay nahi
file =open("test.txt","r")
print(file.read())
file.close()
print("*********************************************")

# A : append
file = open("test.txt","a")
file.write("\nThis is file new Line Appended")
file.close()
print("File Appended Successfully")
print("*********************************************")

file=open("demo.txt","w+")
file.write("This is file now Wriitem Through W+ mode.")
print("Current File Position : ",file.tell())
#position change kari dese
file.seek(0)
print(file.read())
file.close()
print("*********************************************")

