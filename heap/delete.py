def bubbleDown(a,i):
    left = 2 * i + 1
    right = 2 * i + 2
    if(left > len(a) or right > len(a)):
        return
    if(left < len(a) and right > len(a)):
        if(a[left] < a[i]):
            a[left], a[i] = a[i], a[left]
            bubbleDown(a,left)
    else:
        small = 0
        if(a[left] < a[right]):
            small = left
        else:
            small = right
        a[i],a[small] = a[small],a[i]
        bubbleDown(a,small)
    return a

def bubbleUp(arr,j):
    p = (j-1)//2
    
    if(p>=0):
        if(arr[p]>arr[j]):
            arr[p],arr[j] = arr[j], arr[p]
            bubbleUp(arr,p)
    return arr

def deleteHeap(arr,i):
    if i<0 or i>len(arr) - 1:
        return 
    else:
        last = arr.pop()
        arr[i] = last
        return arr

# def heapfy(arr,i):
#     parent = int((i-1)/2)
#     if arr[i] < parent:
#         bubbleUp(arr,i)
#     else:
#         bubbleDown(arr,i)
#     return arr
i = 0
arr = [1,1,2,9,110]
ans1 = deleteHeap(arr,0)
print(ans1)
parent = int((i-1)/2)
child1 = 2 * i + 1
child2 = 2 * i + 2
if ans1[i] > child1 or ans1[i] > child2:
    ans = bubbleDown(ans1,i)
print(ans)
# print(heapfy(ans1,0))