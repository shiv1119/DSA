def insert(arr,j):
    for i in range(j-1,-1,-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[j]
        else:
            break

def isort(arr):
    for i in range(len(arr)):
        insert(arr,i)
    return arr


def bsearch(arr,target,left,right):
    if right >= left:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] > target:
                right = mid - 1
                return bsearch(arr,target,left,right)
            else:
                left = mid+1
                return bsearch(arr,target,left,right)
    else:
        return -1
    
    
arr = [4,2,10,5,7]
arr_sorted = isort(arr)
left = 0
right = len(arr)-1

ans = bsearch(arr_sorted,11,left,right)
print(ans)
            