'''
An Excpetion is an a normal conidtion that aries
during the run time a prgoram

program run ho gaya error Excpetion
Handling : excepetion handle karva
sytem error : prgroam run karva de nahi
10/0 : error solve

program excpetion jarur lage try and catch


'''

'''
print("Start Code")

a =int(input("Enter A:"))
b= int(input("Enter B:"))
#division by zero
c=a/b
print("Division : ",c)
print("End Code")

'''


print("Start Code")
try:
    a =int(input("Enter A:"))
    b= int(input("Enter B:"))
    #division by zero
    c=a/b
    print("Division : ",c)
except:
    # error ne caught kari lidhi
    print("Exception caught")
print("End Code")

