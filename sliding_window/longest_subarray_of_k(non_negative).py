class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        max_len = 0
        seen = dict()
        prefix_sum = 0
        for i in range(n):
            prefix_sum += arr[i]
            
            #case 1: when sum from 0 to 1 exactly equal to k
            if prefix_sum == k:
                max_len = i+1
                
            #case 2: sum of subarray [j+1...i] == k
            
            if (prefix_sum - k) in seen:
                length = i - seen[prefix_sum - k]
                max_len = max(max_len, length)
                
            if prefix_sum not in seen:
                seen[prefix_sum] = i
        
        return max_len