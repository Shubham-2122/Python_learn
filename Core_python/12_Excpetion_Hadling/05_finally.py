'''
    finally is block of code that will
    be excute every time whether excetion
    or not

    error aven na finally genreate thase
    Database opartion open and close
    
'''

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
except Exception as e:
    print("Exception caught :",e)
finally:
    print("Finally Block")
    
print("End Code")
 

