class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()

        p_point, t_point = 0, 0
        while p_point < len(players) and t_point < len(trainers):
            if players[p_point] <= trainers[t_point]:
                p_point += 1
                t_point += 1
            else:
                t_point += 1
        return p_point
