class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        neighbours = dict()  # { node : list of neighbours }
        occurrences = dict()  # { node : # of times it occurs i.e. pointers }

        for i in range(n):
            occurrences[i] = 0
            neighbours[i] = []

        for edge in edges:
            u, v = edge
            occurrences[u] += 1
            occurrences[v] += 1
            neighbours[u].append(v)
            neighbours[v].append(u)

        while len(occurrences) > 2:
            current_keys = list(occurrences.keys())
            decrement = []

            for i in current_keys:
                if occurrences[i] == 1:
                    occurrences.pop(i)  # remove the leave
                    for neighbour in neighbours[i]:  # for each of i's neighbours
                        decrement.append(neighbour)
                        neighbours[neighbour].remove(i)
                    neighbours.pop(i)

            for i in decrement:
                occurrences[i] -= 1
        return list(occurrences.keys())

        # for i in range(len(occurrences)):
        #     if occurrences[i] == 1:
        #         queue.append((i, 0))
        #         visited[i] = True
        #         depths[i] = 0

        # neighbours = dict()  # { node : list of neighbours }
        # occurrences = dict()  # { node : # of times it occurs i.e. pointers }
        # depths = dict()  # { node : minimum depth i.e. fastest time it's reached }
        #
        # for i in range(n):
        #     occurrences[i] = 0
        #     neighbours[i] = []
        #     depths[i] = float('inf')
        #
        # for edge in edges:
        #     u, v = edge
        #     occurrences[u] += 1
        #     occurrences[v] += 1
        #     neighbours[u].append(v)
        #     neighbours[v].append(u)
        #
        # queue = []  # node, depth
        # visited = [False] * n
        #
        # for i in range(len(occurrences)):
        #     if occurrences[i] == 1:
        #         queue.append((i, 0))
        #         visited[i] = True
        #         depths[i] = 0
        #
        # while len(queue) != 0:
        #     node, depth = queue.pop(0)
        #     current_neighbours = neighbours.get(node)
        #     for neighbour in current_neighbours:
        #         if not visited[neighbour]:
        #             queue.append((neighbour, depth + 1))
        #             visited[neighbour] = True
        #             depths[neighbour] = min(depths.get(neighbour), depth + 1)
        #
        # max_depth = max(depths.values())
        # values = list(depths.values())
        # roots = [values.index(max_depth)]
        # for i in range(roots[0] + 1, n):
        #     if values[i] == max_depth:
        #         roots.append(i)
        # return roots
