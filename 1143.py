class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        text1_arr = list(text1)
        text2_arr = list(text2)

        r, c = len(text1_arr), len(text2_arr)
        dp = [[0 for i in range(c + 1)] for i in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if text1_arr[i - 1] == text2_arr[j - 1]:
                    # match made which means can increase LCS
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # else, the longest one is either including the last from text1 or text2
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
        return dp[r][c]
