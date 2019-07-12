n=int(input())
n=2*n
for i in range(1,n+1):
  if(i%2==1):
    for sp in range(1,n-i):
      print(" ",end="")
    for j in range(1,i+1):
      print("*",end=" ")
  if(i!=n):
    print()
l=n
k=1
while(l>0):
  if(l%2==1):
    for sp in range(1,2*k+1):
      print(" ",end="")
    for j in range(1,n-(2*k)):
      print("*",end=" ")
    
    k+=1;
  l-=1
  print()

