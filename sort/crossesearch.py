def crossSearch(x,y,left,right):
    # xi >= yi but yi+1 > xi+1
    
    if right >= left:
        mid = (left + right) // 2
        if x[mid] >= y[mid] and x[mid+1] < y[mid+1]:
            return mid
        else:
            if x[mid] < y[mid]:
                right = mid - 1
                return crossSearch(x,y,left,right)
            else:
                left = mid + 1
                crossSearch(x,y,left,right)
    else:
        return -1
    
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [-2, 0, 4, 5, 6, 7, 8, 9]

print(crossSearch(x,y,0,len(x) - 1))
