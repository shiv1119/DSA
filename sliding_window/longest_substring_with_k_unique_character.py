class Solution:
    def longestKSubstr(self, s, k):
        # code here
        max_len = -1
        h = {}
        i, j = 0, 0
        for j in range(len(s)):
            if s[j] not in h:
                h[s[j]] = 0
            h[s[j]] += 1
            if len(h) == k:
                max_len = max(max_len, j-i+1)
            elif len(h) > k:
                while len(h) > k:
                    h[s[i]] -= 1
                    if h[s[i]] == 0:
                        del h[s[i]]
                    i += 1
                
        
        return max_len
        
        