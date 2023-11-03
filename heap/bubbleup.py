def bubbleUp(a,j):
    
    if j<=0:
        return 
    else:
        if(a[j] < a[j//2]):
            a[j],a[j//2] = a[j//2],a[j]
            bubbleUp(a,j//2)
            
    return a
    
    
    
    # worst case time - depth of heap( no of levels ) - log base 2 n
    
    
    
    
arr = [2,3,7,4,5,9,11,1,8]
print(bubbleUp(arr,7))