rno = int(input("Enter your Roll no : "))
sname = input("Enter your Name : ")
s1 = int(input("Enter your subject 1 :"))
s2 = int(input("Enter your subject 2 :"))
s3 = int(input("Enter your subject 3 :"))

total = s1+s2+s3
per = total/3

print("Roll no :",rno)
print("Student Name :",sname)
print("Total marks : ",total)
print("percentage : ",per)

if per >= 70:
    print("A grade Student :")
elif per >=60:
    print("B grade Student :")
elif per >= 50:
    print("C grade Student :")
elif per >= 40:
    print("C grade Student :")
else:
    print("Fail Student")
