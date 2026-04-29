def test(a,b,c,*d):
    print("a :",a,"b :",b,"c :",c,"d :",d)

test(1,2,3,4)
# tuple store in last value
# last store kar skte he
test(1,2,3,4,5,6,7,8,9)


def demo(a,b,c,*d,**e):
    print("a :",a,"b :",b,"c :",c,"d :",d,"e :",e)

# ** meaing last diconry
demo(1,2,3,4,5,6,7,8,x=10,y=20,z=30)
