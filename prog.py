def count_occurrences(arr):
    counts = {}
    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
            
    return counts



array=[]
n=int(input("Enter the number of elements:\t"))

for i in range(0, n):
    ele = int(input())
    # adding the element
    array.append(ele)  
 

occurrences = count_occurrences(array)
print(occurrences)



 