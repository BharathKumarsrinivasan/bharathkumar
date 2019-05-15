a=-1
while(a==-1):
    try:
        a=int(input("Enter value of a"))
    except:
        print("enter a digit for a")
b=-1
while(b==-1):
    try:
        b=int(input("Enter value of b"))
    except:
        print("Enter a digit for b")
c=int(input("Enter 1.add,2.sub,3.mul,4.div"))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    try:
        print(a/b)
    except:
        while(b==0 or( b>='a' and b>='z') or ( b>='A' and b>='Z') ):
            print("we cant divide by zero please enter diff value")
            b=input()
        print(a/int(b))
    

