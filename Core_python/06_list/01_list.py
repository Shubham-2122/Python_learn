'''
    list : group of different type data
            int,float,char,string,boolean
     list []
     ,data index start 0

     list ma lib function
'''
l =[1,2,1.1,2.2,"tops",True,1,2,10,"python",False]

print(l)
print(len(l))

#list lib function
l.append(100)
print(l)

#list clear : empty data
#l.clear()
#print(l)

#list copy
l1 = l.copy()
print(l1)

#only other append l1, L original update not
l1.append(200)
print(l)
print(l1)

#assigen both in append data l2 and l
l2 = l
print(l2)
l2.append(300)
print(l2)
print(l)

# number 3 resosn 1 is true = 1
print(l.count(1))
print(l.count(1.1))

#extend using list marge
l3=[1000,2000,3000]
print(l3)
l.extend(l3)
print(l)

#index find
print(l.index(10))

#instert (index number,value)
l.insert(5,101)
print(l)

#pop last element remove
l.pop()
print(l)
#pop index number remove
l.pop(10)
print(l)


#remove value remove thase
l.remove(10)
print(l)

#list reverse order
l.reverse()
print(l)

#collection loop
for i in l:
    print(i)
#check element is there or not
print(101 in l)
