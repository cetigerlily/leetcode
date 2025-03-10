class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result_set = set()
        current = []

        def backtrack():
            if len(current) == k:
                current_sum = 0
                for l in range(k):
                    current_sum += int(current[l])
                if current_sum == n:
                    temp = current[:]
                    temp.sort()
                    temp = "".join(temp)
                    result_set.add(temp)
                return

            for j in range(1, 10):
                if str(j) not in current:
                    current.append(str(j))
                    backtrack()
                    current.pop()
        backtrack()

        result = []
        for i in result_set:
            result.append([int(x) for x in list(i)])
        return result

def main():
    print(Solution().combinationSum3(k=3, n=15))


if __name__ == "__main__":
    main()