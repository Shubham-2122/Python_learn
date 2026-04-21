'''
list slice : index number

'''
l = [1,2,3,1.1,2.2,10,20,"tops",True,False,"python","java",11,12,22,34]

print(len(l))
#5 start index jump 5
print(l[5::5])

#
print(l[1:2:3])
print(l[:3:5])
print(l[::12])
print(l[7:8:9])

print(l[:15:10])
print(l[-16::16])
print(l[-12:-5:5])
print(l[:-1:7])
print(l[::-5])
print(l[-14:-13:5])
