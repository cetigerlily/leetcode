class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)):
            current_char = s[i]
            if current_char == '*':
                result.pop()
            else:
                result.append(current_char)
        return "".join(result)
