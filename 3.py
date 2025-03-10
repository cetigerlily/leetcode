class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        result = 0
        existing = set()
        for i in range(len(s)):
            character = s[i]
            if character not in existing:
                existing.add(character)
                result = max(result, i - start + 1)
            else:
                # need to move start and remove s[start] until character not in existing
                while character in existing and start < len(s):
                    existing.remove(s[start])
                    start += 1
                existing.add(character)
        return result
