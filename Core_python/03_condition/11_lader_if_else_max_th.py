a = int(input("Enter your A : "))
b = int(input("Enter your B : "))
c = int(input("Enter your C : "))

if a > b:
    if a > c:
        print("A is Max :",a)
    else:
        print("C is Max :",c)
elif b > c:
    print("B is Max :",b)
else:
    print("C is Max :",c)
