'''
    fucntion ni under function ek argument hase
'''
def my_decorator(func):
    def wrapper():
        print("Before calling the funtion")
        func() # call the original function
        print("After Calling the function")

    return wrapper # Return the wrapper function

@my_decorator
def say_hello():
    print("Hello , world")

say_hello()
