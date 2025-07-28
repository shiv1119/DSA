class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

#printing longest common subsequence

def findLCS(m: int, n: int, s1: str, s2: str) -> str:
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    i = m
    j = n
    lcs = []

    while(i > 0 and j > 0):
        if(s1[i-1] == s2[j-1]):
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j -= 1
            else:
                i -= 1
    print("".join(reversed(lcs)))
    return "".join(reversed(lcs))
