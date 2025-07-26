#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        i = 0
        j = 0
        _sum = 0
        max_sum = float("-inf")
        
        while j < len(arr):
            _sum += arr[j]
            
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                max_sum = max(max_sum, _sum)
                _sum -= arr[i]
                i += 1
                j += 1
        return max_sum