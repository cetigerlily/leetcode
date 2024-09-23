class Solution(object):
    def BFS(self, index, isConnected, visited):
        queue = [index]
        while len(queue) != 0:
            current = queue.pop(0)
            # if not visited[current]:
            for i in range(len(isConnected)):
                if not visited[i] and isConnected[current][i] == 1:
                    queue.append(i)
                    visited[i] = True

        return visited


    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False for i in range(n)]
        count = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count += 1
                visited = Solution().BFS(i, isConnected, visited)

        return count
