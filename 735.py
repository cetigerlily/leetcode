class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []  # pop() removes last item and append adds to end i.e. a stack
        for i in range(len(asteroids)):
            asteroid = asteroids[i]
            while result and asteroid < 0 < result[-1]:  # while result not empty and asteroid neg and top is pos
                # handle collisions
                if abs(asteroid) > abs(result[-1]):  # asteroid > top so remove and continue checking
                    result.pop()
                    continue
                elif abs(asteroid) == abs(result[-1]):
                    result.pop()
                break
            else:
                result.append(asteroid)

        return result
