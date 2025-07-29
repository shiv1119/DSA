# User function Template for python3
class Solution:
    def minOperations(self, s1, s2):
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        no_deletion = m - dp[m][n]  # string 1 minus LCS length will give us no of deletion
        no_insertion = n - dp[m][n]  # string 2 minus LCS length will give us no of insertion
        
        return no_deletion + no_insertion
