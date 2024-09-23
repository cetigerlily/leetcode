import math

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        num_spells = len(spells)
        num_potions = len(potions)

        pairs = [0 for i in range(num_spells)]
        potions = sorted(potions)

        for i in range(num_spells):
            spell_strength = spells[i]
            min_pair = math.ceil(success / spell_strength)
            if potions[-1] < min_pair:
                pairs[i] = 0
            else:
                start, end = 0, num_potions - 1
                while start <= end:
                    mid_index = math.floor((start + end) / 2)
                    if potions[mid_index] * spell_strength >= success:
                        end = mid_index - 1
                    else:
                        start = mid_index + 1
                # start finds the first index when it satisfies
                if potions[start] * spell_strength >= success:
                    pairs[i] = num_potions - start
        return pairs
