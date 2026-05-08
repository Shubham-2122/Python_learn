# file under string allow 

file =open("data.txt","w")
for i in range(1,11):
    file.write(str(i)+",")
file.close()
print("suucess fully print")

#file read thei
file = open("data.txt","r")
even = open("even.txt","w")
odd = open("odd.txt","w")

l = file.read().split(",")[:-1]
#list
print(l)
for i in l:
    if int(i)%2 ==0:
        even.write(i+",")
    else:
        odd.write(i+",")
file.close()
even.close()
odd.close()

print("Data file Content")
file = open("data.txt","r")
print(file.read())
file.close()

print("Even file Content")
even = open("even.txt","r")
print(even.read())
even.close()

print("Odd file Content")
odd = open("odd.txt","r")
print(odd.read())
odd.close()

