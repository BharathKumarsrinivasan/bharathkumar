n,v=map(int,input().split(" "))
set=list(map(int,input().split()))
subset=list(map(int,input().split()))
z=0
for i in range(0,len(subset)):
    if subset[i] in set:
        z=z+1
if len(subset)==z:
    print("YES")
else:
    print("NO")
