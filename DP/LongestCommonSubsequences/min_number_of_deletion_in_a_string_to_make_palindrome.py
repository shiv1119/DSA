#TLE
class Solution:
    def minDeletions(self, s):
        # code here
        s_rev = s[::-1]
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return n - dp[n][n]
     
# Not tle
# class Solution:
#     def minDeletions(self, S): 
#         def longest_palindromic_subsequence_length(S):
#             n = len(S)
#             dp = [[0] * n for _ in range(n)]
#             for i in range(n):
#                 dp[i][i] = 1
#             for cl in range(2, n + 1):
#                 for i in range(n - cl + 1):
#                     j = i + cl - 1
#                     if S[i] == S[j]:
#                         dp[i][j] = 2 + dp[i + 1][j - 1]
#                     else:
#                         dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
#             return dp[0][n - 1]
#         n = len(S)
#         lps_length = longest_palindromic_subsequence_length(S)
#         return n - lps_length
