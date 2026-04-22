'''
A set is a collection of:
Unique elements
Unordered
Mutable (you can change it)
 {}
'''
# only store unique duplicate remove
s = {1,2,2,3,4}
print(s)

s.add(5)
print(s)

#value update
s.update([2,6])
print(s)

#value remove
s.remove(2)
print(s)

#discard value
s.discard(5)
print(s)

#first element remove
s.pop()
s.pop()
print(s)

