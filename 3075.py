class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        happiness_sum = 0
        for i in range(k):
            if happiness[i] - i > 0:
                happiness_sum += happiness[i] - i
        return happiness_sum
