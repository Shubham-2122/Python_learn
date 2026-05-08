print("Start Code")
try:
    a =int(input("Enter A:"))
    b= int(input("Enter B:"))
    #division by zero
    c=a/b
    print("Division : ",c)
    #10/0
except ZeroDivisionError as e:
    # error ne caught kari lidhi
    print("Exception caught :",e)
    #10.10
except ValueError as e:
    # error ne caught kari lidhi
    print("Exception caught :",e)
print("End Code")
