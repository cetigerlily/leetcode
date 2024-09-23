class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = ""
        for i in range(len(s)):
            result += str(ord(s[i]) - 96)

        for i in range(k):
            digits = list(result)
            new_result = 0
            for digit in digits:
                new_result += int(digit)
            result = str(new_result)
        return int(result)
