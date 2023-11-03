def heapify(arr,i): #lg(n)
    parent = int((i-1)/2)
    left = 2*i + 1
    right = 2 * i + 2
    n = len(arr)
    if left < n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i],arr[largest] = arr[largest], arr[i]
        heapify(arr,largest)
     
def buildMaxHeapify(arr):
    n = len(arr) // 2
    for i in range(n-1,-1,-1): #(n) Over all(n lg(n))
          heapify(arr,i)
    
        
arr = [9,4,2,6,7,10,67,45,23,15,2,199,45,62,10,24]
buildMaxHeapify(arr)
print(arr)