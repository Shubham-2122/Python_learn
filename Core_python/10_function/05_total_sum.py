 
'''
5! = 5*4*3*2*1 = 120
'''

num = int(input("Enter your number :"))

def total(n):
    suma = 0;
    for i in range(1,n+1):
        suma = suma + i
    return suma

print("Num of value :",num)
print("num of total sum :",total(num))
