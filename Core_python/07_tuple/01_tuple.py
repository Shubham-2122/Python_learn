'''
tuple : group of mix type of data
tuple : we can not change
      : add,update,delete
      () will be tuple
      A tuple is a collection of items like a list, but immutable (cannot be changed after creation).
'''
t = (1,2,1.1,2.2,"tops",True,"python",1,1,False)

print(t)
#totle count
print(t.count(1))

#value number of index show
print(t.index(0))

#tuple for loop
print("tuple show loop")
for i in t:
    print(i)
