class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        s_pointer = 0
        try:
            t_pointer = t.index(s[s_pointer])  # starting search at the first occurrence of s[i] letter
            while t_pointer < len(t):
                if s[s_pointer] == t[t_pointer]:
                    s_pointer += 1
                    if s_pointer > len(s) - 1:
                        return True
                t_pointer += 1
            return False
        except ValueError:
            return False  # first letter s is not even in t
