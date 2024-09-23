class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        start_pointer = 0
        end_pointer = len(s) - 1
        s = list(s)

        print(len(s))
        print(s[0])
        for i in range(len(s)):
            if start_pointer <= len(s) - 1 and end_pointer >= 0:
                while s[start_pointer] not in vowels and start_pointer + 1 <= len(s) - 1:
                    start_pointer += 1
                while s[end_pointer] not in vowels and end_pointer - 1 >= 0:
                    end_pointer -= 1
                if start_pointer > end_pointer:
                    break

                start_letter = s[start_pointer]
                end_letter = s[end_pointer]

                s[start_pointer] = end_letter
                s[end_pointer] = start_letter
                start_pointer += 1
                end_pointer -= 1

        return "".join(s)
