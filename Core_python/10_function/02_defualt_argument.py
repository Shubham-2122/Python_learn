
def test(a=10,b=20,c=30,d=40):
    print("a :",a,"b :",b,"c :",c,"d :",d)

test(1,2,3,4)
# paramter value defualt pass na kari argument pass kari
test(10,20,30)

# value pass kari
test(10,20,30,40)

# 2 defualt
test(10,20)

# 2 argument b and d
test(b=30,d=80)

def Info(name="Guest"):
    print("Name : ",name)

Info()
Info("shubham")

