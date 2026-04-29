'''
    function : it's block of code when we need use it. call it

    1) libriy function : predefined
        string,tuple,list . 
    2) user defined function
        return type allow nathi
        cate
        1) function with no agrument & no return value.
        2) function with agrument & no return value
        3) function with agrument & no return value
'''

#function with no agrument & no return value.
def printLine():
    print("*"*50)

#call function
printLine()
print("hello shubham")
printLine()


# function with agrument & no return value
def add(a,b):
    print("sum :",a+b)
    
printLine()
add(20,10)
printLine()

# function with agrument & with return value
def sub(a,b):
    return a-b

printLine()
print("sub : ",sub(30,20))
printLine()





