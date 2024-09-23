class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        indegree = [0 for i in range(numCourses)]
        neighbors = [[] for i in range(numCourses)]
        for prereq in prerequisites:
            a, b = prereq
            neighbors[b].append(a)
            indegree[a] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        courses_reached = 0
        while len(queue) != 0:
            current = queue.pop(0)
            courses_reached += 1
            for neighbor in neighbors[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return courses_reached == numCourses
