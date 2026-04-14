'''
1
2 3
4 5 6
'''
#n = int(input("Enter your number row :"))
num = 1
n = 4 # number of row

for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
