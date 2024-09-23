# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            if guess(n) == 0:
                return n
            else:
                return n - 1

        start, end = 1, n
        while start <= end:
            middle = int(floor((start + end) / 2))
            result = guess(middle)

            if result == 0:
                return middle
            elif result == 1:
                start = middle + 1
            elif result == -1:
                end = middle - 1
