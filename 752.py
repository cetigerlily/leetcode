class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def get_neighbours(current):  # input as a string "XXXX"
            valid_neighbours = []
            for k in range(4):  # for each wheel
                new_neighbour = current[:]

                for change in [-1, 1]:
                    new_neighbour = new_neighbour[:k] + str((int(current[k]) + change) % 10) + new_neighbour[k + 1:]
                    valid_neighbours.append(new_neighbour)
            return valid_neighbours

        if "0000" == target:
            return 0

        if "0000" in deadends:
            return -1

        source = "0000"
        queue = [(source, 0)]  # (code, distance from source)

        visited = set(deadends)
        visited.add(source)

        while len(queue) != 0:
            current_code, current_distance = queue.pop(0)
            if current_code == target:
                return current_distance

            neighbours = get_neighbours(current_code)
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append((neighbour, current_distance + 1))
                    visited.add(neighbour)
        return -1

    # def get_neighbours(current):  # get neighbours when converting each digit into an int array
    #     valid_neighbours = []
    #     for k in range(4):  # for each wheel
    #         neighbour_down = current[:]
    #         neighbour_up = current[:]
    #         current_wheel = current[k]
    #
    #         if current_wheel == 0:
    #             new_down = 9
    #             new_up = 1
    #         elif current_wheel == 9:
    #             new_down = 8
    #             new_up = 0
    #         else:
    #             new_down = current[k] - 1
    #             new_up = current[k] + 1
    #
    #         neighbour_down[k] = new_down
    #         neighbour_up[k] = new_up
    #
    #         valid_neighbours.append(neighbour_down)
    #         valid_neighbours.append(neighbour_up)
    #     return valid_neighbours
