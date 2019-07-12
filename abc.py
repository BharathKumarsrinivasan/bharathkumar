n=int(input())
s="abcdefghijklmnopqrstuvwxyz"
s=s.upper()
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    print(s[:i][::-1])
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    print(s[:i][::-1])
