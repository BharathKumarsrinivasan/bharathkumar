val1,val2,val3=input().split()
val1=int(val1)
val2=int(val2)
val3=int(val3)
if(val1>val2 and val1>val3):
    print(val1)
elif(val2>val3):
    print(val2)
else:
    print(val3)
