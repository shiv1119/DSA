def bubbleDown(a,i):
    left = 2 * i + 1
    right = 2 * i + 2
    if(left > len(a)):
        return
    if(left <= len(a) and right > len(a)):
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
arr = [15,2,5,9,11,5,6,12,19]
print(bubbleDown(arr,0))
#  log(n)