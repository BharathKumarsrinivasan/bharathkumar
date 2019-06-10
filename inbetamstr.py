n,m=map(int,input().split())


for num in range(n,m):
    l=len(str(num))
    sum=0
    temp=num
    while(num>0):
        x=num%10
        sum=sum+(x**l)
        num=num//10
    if(sum==temp):
        print(sum,end=" ")
