n=int(input())
l=[]
for i in range(n):
    l.append(input())
sorted(l)
m=len(l[0])
st=""
c=l[0]
for i in range(m):
    a=True
    for x in l:
        if x[i]!=c[i]:
            a=False
            break
    if a:
        st=st+c[i]
    else:
        break
print(st)
