def heapify(arr,n,i):
    parent = int((i-1)/2)
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    else:
        largest = i
    
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)
        
def buildMaxHeap(arr):
    n = len(arr)
    m = n // 2
    for i in range(m-1,-1,-1):
        heapify(arr,n,i)
        
        
def heapSort(arr):
    buildMaxHeap(arr)
    n = len(arr)
    for i in range(n-1,0,-1):
        
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
        
arr = [6, 5, 45, 78, 45, 64, 23, 12, 2, 56]
heapSort(arr)
print(arr)