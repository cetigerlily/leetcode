class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # [0, 1, 2, 3] = [north, east, south, west]
        directions = { 0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

        def update_direction(current_direction, rotation):
            if rotation == -2:  # turning L
                if current_direction == 0:
                    return 3
                return current_direction - 1
            elif rotation == -1:  # turning R
                if current_direction == 3:
                    return 0
                return current_direction + 1

        set_obstacles = set()
        for obstacle in obstacles:
            set_obstacles.add((obstacle[0], obstacle[1]))

        def update_position(current_position, steps, current_direction):
            a, b = current_position
            update = directions[current_direction]
            while steps > 0:
                if (a + update[0], b + update[1]) in set_obstacles:
                    break
                else:
                    a += update[0]
                    b += update[1]
                steps -= 1
            return (a, b)

        def get_euclidean_distance(current_position):
            return (current_position[0]) ** 2 + (current_position[1]) ** 2

        position = (0, 0)
        max_distance = 0
        direction = 0
        for command in commands:
            if command == -2:
                direction = update_direction(direction, -2)
            elif command == -1:
                direction = update_direction(direction, -1)
            else:
                position = update_position(position, command, direction)
                distance = get_euclidean_distance(position)
                if distance > max_distance:
                    max_distance = distance
                    # max_position = position

        return max_distance
