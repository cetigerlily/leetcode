class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        s = s.lower()

        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                letter_i = s[i]
                letter_j = s[j]
                if letter_i != letter_j:
                    return False
                i += 1
                j -= 1
        return True
