def missing(arr):
    
    if arr==2:
        return 1
    else:
     n= len(arr)+1
     total_sum=n*(n+1)//2
     actual_sum=sum(arr)
     missing=total_sum-actual_sum 
    
     return missing 
 


array=[]
n=int(input("Enter the number of elements:\t"))

for i in range(0, n):
    ele = int(input())
    # adding the element
    array.append(ele)  
 

occurrences = missing(array)
print("missing number is\n",occurrences)
