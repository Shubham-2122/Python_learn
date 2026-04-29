'''
    0 1 1 2 3 5 8 13 21 34
    𝐹(𝑛)=𝐹(𝑛\−1)+𝐹(𝑛−2),𝐹(0)=0, 𝐹(1)=1
'''

num = int(input("Enter your num : "))

def fibo(n):
    a=0
    b=1
    for i in range(1,n):
        print(a,end=" ")
        a,b=b,a+b

print("number of value :",num)
fibo(num)
