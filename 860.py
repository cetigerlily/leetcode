class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        available_change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            available_change[bill] += 1

            change = bill - 5
            while change > 0:
                if change >= 20 and available_change[20] > 0:
                    change -= 20
                    available_change[20] -= 1
                elif change >= 10 and available_change[10] > 0:
                    change -= 10
                    available_change[10] -= 1
                elif change >= 5 and available_change[5] > 0:
                    change -= 5
                    available_change[5] -= 1
                else:
                    return False
        return True
