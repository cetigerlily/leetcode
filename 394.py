class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        stack = []
        for i in range(len(s)):
            character = s[i]
            if character != "]":  # if it's not a closing bracket, add it to the stack
                stack.append(character)
            else:
                encode = []
                while stack[-1] != "[":  # continue finding the string to repeat
                    encode.insert(0, stack.pop())
                stack.pop()  # pop off [
                k = []
                while stack and stack[-1] in digits:
                    k.insert(0, stack.pop())
                k = int("".join(k))
                encode = "".join(encode)
                for i in range(k):
                    stack.append(encode)
        return "".join(stack)
