import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # n piles of bananas, which each piles[i]
        # guards will come back in h hours

        # eats in k bananas / hour - if pile[i] < k, then will j eat whole pile for the hour
        # min(pile[i], k)

        # find minimum k st can eat all bananas within h hours

        # k is able to be = 1 - max # bananas in pile
        # [1, ..., 11] - start at middle value and determine if enough time
        # if enough time, move search lower to find minimum k
        # if not enough time, increase search to second half
        def get_hours(rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            return hours


        max_pile = max(piles)
        rates = [i for i in range(1, max_pile + 1)]
        start, end = 0, len(rates)
        while start <= end:
            middle = int(math.floor((start + end) / 2))
            total_hours = get_hours(rates[middle])
            if total_hours > h:
                # not enough time so need to move to 2nd 1/2
                start = middle + 1
            else:
                end = middle - 1
        return rates[start]
