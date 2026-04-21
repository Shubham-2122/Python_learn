t = (1,2,1.1,2.2,"tops",[10,20,30],True,"python",1,1,False)

print(t)
#totle count
print(t.count(1))

#value number of index show
print(t.index(0))

#tuple for loop
print("tuple show loop")
for i in t:
    print(i)

#tuple inside list change allowed
#loophold
    
print(t[5])
t[5].append(40)
print(t)

print(10 in t)
