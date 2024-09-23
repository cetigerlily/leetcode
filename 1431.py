class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # n = # of kids with candies
        # candies[i] = # of candies kid i has
        # extraCandies = # of extra candies

        # return result - result[i] = true if giving all
        # extra to kid i means has highest # of
        # candies amongst all kids

        # find max candies[i]
        # result[i] = true if candies[i] + extra > max candies, else false

        local_max = max(candies)
        result = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= local_max:
                result[i] = True
        return result
