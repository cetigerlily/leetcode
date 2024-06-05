class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:  # if the length is odd
            return False

        stack = []
        closing_brackets = [")", "]", "}"]
        opening_brackets = {"(": 0, "[": 1, "{": 2}

        for i in range(len(s)):
            if s[i] in opening_brackets:
                stack.append(s[i])
            else:  # it's a closing bracket, need to check if recent is the matching opening bracket
                if len(stack) == 0:  # reached a closing bracket but there are no openings in the stack thus far
                    return False

                recent = stack[-1]
                matching_closing = closing_brackets[opening_brackets[recent]]
                if s[i] != matching_closing:
                    return False
                stack.pop()

        return len(stack) == 0
