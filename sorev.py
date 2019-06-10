n=int(input())
x=list(map(int,input().split()))
x.sort()
s=x[::-1]
print(*s,sep="")
