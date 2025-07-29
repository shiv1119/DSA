# Length of shortest common super sequence GFG
class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
        #code here
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if(s1[i-1] == s2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return m+n - dp[m][n]
    
# Printing Leetcode  shortest common super sequence

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m = len(str1)
        n = len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        i = m
        j = n
        scs = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                scs.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                scs.append(str1[i-1])
                i -= 1
            else:
                scs.append(str2[j-1])
                j -= 1
        
        while i>0:
            scs.append(str1[i-1])
            i -= 1
        
        while j > 0:
            scs.append(str2[j-1])
            j -= 1
        
        return ''.join(reversed(scs))
         