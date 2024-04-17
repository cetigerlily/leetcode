class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time_before = 0
        for i in range(0, k):
            time_before += min(tickets[i], tickets[k])

        time_after = 0
        for i in range(k + 1, len(tickets)):
            time_after += min(tickets[i], tickets[k] - 1)

        return tickets[k] + time_before + time_after
