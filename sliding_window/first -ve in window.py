#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
        # code here 
        q = deque()
        result = []
        i = 0
        j = 0
        while j < len(arr):
            if arr[j] < 0:
                q.append(arr[j])
            
            if j-i+1 < k:
                j += 1
            elif j-i +1 == k:
                if q:
                    result.append(q[0])
                    if q[0] == arr[i]:
                        q.popleft()
                else:
                    result.append(0)
                i += 1
                j += 1
        
        return result
