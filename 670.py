class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_arr = list(str(num))
        results = set()
        results.add(num)

        for i in range(len(num_arr)):
            max_digit = num_arr[i]
            max_index = i
            for j in range(i, len(num_arr)):
                current = num_arr[j]
                if current >= max_digit:
                    max_digit = current
                    max_index = j

            original = num_arr[i]
            num_arr[i] = max_digit
            num_arr[max_index] = original
            current_result = int("".join(num_arr))
            results.add(current_result)
            # results.append(current_result)

            num_arr[i] = original
            num_arr[max_index] = max_digit

        return max(results)
