class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False for i in range(len(rooms))]

        # def dfs(rooms, index, visited):
        #     visited[index] = True
        #     for key in rooms[index]:
        #         if visited[key] != True:
        #             dfs(rooms, key, visited)
        #     return visited
        #
        # result = set(dfs(rooms, 0, visited))
        # return False not in result

        queue = [0]  # queue of index of rooms
        visited[0] = True

        while len(queue) != 0:
            index = queue.pop(0)
            keys = rooms[index]
            for key in keys:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        result = set(visited)
        return False not in result
