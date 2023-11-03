def insert(arr,j):
    for i in range(j-1,-1,-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            break
    
def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        insert(arr,i)
    return arr

print(insertionSort([10,20,1,15,4,6,90,200,49]))