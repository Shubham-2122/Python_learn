'''
string : group of charctors
'''
s = "Tops Technologies"
print(s)

# length find
print(len(s))

#string lib function
print(s.capitalize())
print(s.casefold())
print(s.upper())
print(s.lower())

#cpital and small change
print(s.swapcase())

# word upper case first
print("pyhton programing".title())

# total charctor in 40 pattern inside name
print(s.center(40,"*"))
print(s.center(40,"-"))

#how may charctors
print(s.count("T"))

#true and false end string match
print(s.endswith("es"))

#index find to log number start index
print(s.find("log"))

# T index start 
print(s.index("T"))

# T index second index start
print(s.index("T",2))

# is codition check function num or char che
print("tops123".isalnum())
print("tops".isalnum())

print("tops".isalpha())
print("123243".isnumeric())

print(s.istitle())
#space yes or no
print(" ".isspace())

#replce char
print("Hello".replace("l","w"))





