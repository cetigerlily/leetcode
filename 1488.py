import heapq
class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        rain_over = {}  # <lake, list of days rained over lake>
        for i in range(len(rains)):
            if rains[i] != 0:
                if rains[i] not in rain_over:
                    rain_over[rains[i]] = []
                rain_over[rains[i]].append(i)

        full = set()
        upcoming_floods = []  # min heap of upcoming days of flooded_lakes, based on lakes which are currently full
        ans = [-1 for i in range(len(rains))]
        for i in range(len(rains)):
            lake = rains[i]
            if lake != 0:
                if lake in full:
                    return []
                else:
                    full.add(lake)
                    rain_over[lake].pop(0)
                    if len(rain_over[lake]) > 0:
                        flood_day = rain_over[lake][0]
                        heapq.heappush(upcoming_floods, (flood_day, lake))
            else:
                if len(upcoming_floods) > 0:
                    flood_day, lake = heapq.heappop(upcoming_floods)
                    full.remove(lake)
                    ans[i] = lake
                else:
                    ans[i] = 1
        return ans
