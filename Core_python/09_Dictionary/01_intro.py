'''
Dictionary : key and value pair
           : it must be unique {}
           : key must be unique
'''
d = {110:"shubham",908:"sujal",346:"papa",321:"mummy",787:"brother",232:"grandfather",343:"grandmother"}

print(d)

# key change name
d[321] = "devedara"
print(d)

#key value get
print(d.get(346))

# key value tuple and list convert kar diya
print(d.items())

#only key check
print(d.keys())

#only value print
print(d.values())

#pair in delete key pass delete
d.pop(232)
print(d)

#last delele thase
d.popitem()
print(d)

# last update value and key
d1 = {232:"het",676:"varj"}
d.update(d1)
print(d)

#loop in key and value
for i in d:
    print(i," : ",d[i])





