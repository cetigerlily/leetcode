class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        num_boats = 0
        i = 0
        j = len(people) - 1
        people.sort()
        saved_people = 0

        while i < j:
            if limit - people[i] < people[i]:
                num_boats += 1
                saved_people += 1
                i += 1
            elif people[i] + people[j] <= limit:
                num_boats += 1
                saved_people += 2
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                j -= 1

        if saved_people < len(people):
            num_boats += len(people) - saved_people
        return num_boats
