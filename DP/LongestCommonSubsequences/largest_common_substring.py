#User function Template for python3

#Returns length
class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_len = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (s1[i-1] == s2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_len = max(max_len, dp[i][j])
        
        return max_len
        
#print
class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        end_pos = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_len = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (s1[i-1] == s2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                    if max_len < dp[i][j]:
                        max_len = dp[i][j]
                        end_pos = i
        
        return s1[end_pos-max_len:end_pos]  