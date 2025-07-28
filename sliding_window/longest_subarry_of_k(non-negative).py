class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        i = 0
        _sum = 0
        max_len = 0

        for j in range(n):
            _sum += arr[j]

            while _sum > k and i <= j:
                _sum -= arr[i]
                i += 1

            if _sum == k:
                max_len = max(max_len, j - i + 1)

        return max_len
