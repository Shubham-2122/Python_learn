'''
    prime number find
'''

num = int(input("Enter your num : "))

def prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print("number of value :",num)
print("it's prime Number : ",prime(num))
