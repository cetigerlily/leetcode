class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        def get_neighbours(mutation):
            valid_neighbours = set()
            changes = ['A', 'C', 'G', 'T']

            for k in range(8):  # for each letter in gene mutation
                current_letter = mutation[k]
                for change in changes:
                    if current_letter != change:
                        new_neighbour = mutation[:k] + change + mutation[k + 1:]
                        if new_neighbour in bank:
                            valid_neighbours.add(new_neighbour)
            return valid_neighbours

        if startGene == endGene:
            return 0

        if endGene not in bank:  # if the end gene isn't valid, there's no way to reach it
            return -1

        queue = [(startGene, 0)]
        visited = [startGene]

        while len(queue) != 0:
            current_gene, current_distance = queue.pop(0)
            if current_gene == endGene:
                return current_distance

            neighbours = get_neighbours(current_gene)
            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour, current_distance + 1))
        return -1
