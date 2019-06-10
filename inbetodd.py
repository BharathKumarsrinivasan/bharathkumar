start,end=input().split()

start=int(start)+1

end=int(end)

for num in range(start,end): 
    if(num%2 != 0): 
        print(num, end=" ")
