class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total_black = 0
        min_steps = 0
        for i in range(n):
            if s[i] == "1":
                total_black += 1
            else:
                min_steps += total_black
        return min_steps
