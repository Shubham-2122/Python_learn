 
'''
5! = 5*4*3*2*1 = 120
n!=n×(n−1)×(n−2)×⋯×1

'''

num = int(input("Enter your number :"))

def factroial(n):
    fact = 1;
    for i in range(1,n+1):
        fact = fact * i
    return fact

print("Num of value :",num)
print("num of fatorial :",factroial(num))
