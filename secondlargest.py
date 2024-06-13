n=int(input("Enter a number"))
var=0

array=[]

for i in range(n):
    elem=int(input())
    array.append(elem)
    array.sort()
    
    print(array)   
    

for i in range(n):
    if array[n-1]>array[n-2]:
        var=array[n-1]
        

    else:
        var2=array[n-2]

print(var)