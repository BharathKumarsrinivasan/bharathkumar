n1 = input()
n2 = input()
n3 =input()
 
if (n1 > n2) and (n1 > n3):
   larg = n1
elif (n2 > n1) and (n2 > n3):
   larg = n2
else:
   larg = n3
 
print(larg)
