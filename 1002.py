class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        min_freq = [float('inf')] * 26
        for word in words:
            current_freq = [0] * 26
            for i in range(len(word)):
                current_freq[ord(word[i]) - ord('a')] += 1

            for i in range(26):
                min_freq[i] = min(min_freq[i], current_freq[i])

        common_characters = []
        for i in range(26):
            if min_freq[i] != 0:
                character = chr(i + ord('a'))
                for j in range(min_freq[i]):
                    common_characters.append(character)
        return common_characters
