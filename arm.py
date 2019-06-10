A=int(input())

temp=A
arm=0
while(A!=0):
	rem=A%10
	arm=arm+(rem**3)
	A=A//10
if(temp==arm):
	print('yes')
else:
	print('no')
