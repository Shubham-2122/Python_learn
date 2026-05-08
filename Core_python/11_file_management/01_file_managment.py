'''
File Mangement : file oparation read,write

file : need log entry
     : database import and export

'''
#write karva mate
file =open("test.txt","w")
file.write("this is file test data")
file.close()
print("File Written success")
print("*********************************************")

#file read mode
file =open("test.txt","r")
print(file.read())
file.close()
print("*********************************************")

#file append data file add data
file =open("test.txt","a")
file.write("\nThis is File Shubham jadav append data.")
file.close()
print("File Data Append Success")

#file append thay pachi read file
file =open("test.txt","r")
print(file.read())
file.close()
print("*********************************************")


#w+ : write and read
file=open("tops.txt","w+")
file.write("This Is file Write and read mode")
print("current file location",file.tell())
# seek curser point change karva
file.seek(0)
print(file.read())
file.close()
print("*********************************************")


#r+ : read and write
