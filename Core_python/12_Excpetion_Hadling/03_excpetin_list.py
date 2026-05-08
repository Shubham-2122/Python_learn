print("Start Code")
try:
    a =int(input("Enter A:"))
    b= int(input("Enter B:"))
    #division by zero
    c=a/b
    print("Division : ",c)
    l=[1,2,3,4,5]
    index = int(input("Enter Index Number : "))
    print(l[index])
except IndexError as d:
    print("exception caught : ",d)
except ZeroDivisionError as e:
    # error ne caught kari lidhi
    print("Exception caught :",e)
except ValueError as e:
    # error ne caught kari lidhi
    print("Exception caught :",e)
print("End Code")
 

