n=int(input("Enter a number"))
flag=0
array=[]

for i in range(n):
    elem=int(input())
    array.append(elem)

for i in range(0,n-1):
    if array[i]==array[i+1]:
        flag=1
        print(array[i])
    
if flag==0:
    print(-1)
    