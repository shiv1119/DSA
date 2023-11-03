def bubbleUp(arr,j):
    p = (j-1)//2
    
    if(p>=0):
        if(arr[p]>arr[j]):
            arr[p],arr[j] = arr[j], arr[p]
            bubbleUp(arr,p)
    return arr


def insert(heap,ele):
    heap.append(ele)
    return heap


hp = [1, 2, 7, 3, 5, 9, 11, 4, 8]
# log(n)
ans1 = insert(hp,3)
print(ans1)
print( bubbleUp(ans1,9))

