class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = [0]
        for i in range(len(gain)):
            altitude.append(altitude[i] + gain[i])
        return max(altitude)
