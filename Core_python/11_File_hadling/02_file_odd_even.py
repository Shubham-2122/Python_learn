file=open("data.txt","w")
for i in range(1,11):
    file.write(str(i)+",")
file.close()

file=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

l = file.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
file.close()
even.close()
odd.close()

print("Data File Content")
file = open("data.txt","r")
print(file.read())
file.close()

print("even File Content")
even = open("even.txt","r")
print(even.read())
even.close()


print("odd File Content")
odd = open("odd.txt","r")
print(odd.read())
odd.close()
