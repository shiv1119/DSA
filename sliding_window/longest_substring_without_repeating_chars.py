from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        h = defaultdict(int)

        for j in range(len(s)):
            h[s[j]] += 1

            if len(h) == j-i+1:
                max_len = max(max_len, j-i+1)
            elif len(h) < j-i+1:
                while len(h) < j-i+1:
                    h[s[i]] -= 1
                    if h[s[i]] == 0:
                        del h[s[i]]
                    i += 1
        
        return max_len
        