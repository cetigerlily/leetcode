class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        queue = []
        visited = set()  # have explored with BFS
        length = {}  # <sum node, length to reach that sum node>

        for coin in coins:
            queue.append(coin)
            visited.add(coin)
            length[coin] = 0

        while len(queue) != 0:
            current_sum = queue.pop(0)
            if current_sum == amount:
                return length[current_sum] + 1

            for coin in coins:
                neighbor_sum = current_sum + coin
                if neighbor_sum not in visited and neighbor_sum <= amount:
                    visited.add(neighbor_sum)
                    queue.append(neighbor_sum)
                    length[neighbor_sum] = length[current_sum] + 1

        return -1
