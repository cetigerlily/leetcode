class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) < 1:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        digits = list(digits)
        result = []
        permutation = []

        def backtrack(current_digit):
            if len(permutation) == len(digits):
                result.append("".join(permutation))
                return

            current_letters = mapping[digits[current_digit]]
            for letter in current_letters:
                permutation.append(letter)
                backtrack(current_digit + 1)
                permutation.pop()

        backtrack(current_digit=0)
        return result
