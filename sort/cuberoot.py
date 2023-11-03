def cuberoot(x,left,right):
    cube = lambda x: x * x * x
    if right >= left:
        mid = (left+right) // 2
        cb1 = cube(mid)
        cb2 = cube((mid+1))
        if cb1 <= x and cb2 > x:
            return mid
        else:
            if cb1>x:
                right = mid - 1
                return cuberoot(x,left,right)
            else:
                left = mid + 1
                return cuberoot(x,left,right)
    else:
        return -1
    
print(cuberoot(8,0,7))
    