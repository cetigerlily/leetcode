class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        sum_m = sum(rolls)
        m = len(rolls)

        sum_n = mean * (m + n) - sum_m
        if sum_n < n or sum_n > (n * 6):
            return []

        result = [1 for i in range(n)]
        sum_n -= n

        for i in range(len(result)):  # O(n)
            amount_to_add = min(5, sum_n)
            result[i] += amount_to_add
            sum_n -= amount_to_add

            if sum_n <= 0:  # no more to add
                break
        return result
