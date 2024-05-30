class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def get_area(start_index, end_index):
            area_height = min(height[start_index], height[end_index])
            area_width = abs(end_index - start_index)
            return area_width * area_height

        start_pointer = 0
        end_pointer = len(height) - 1
        max_area = get_area(start_pointer, end_pointer)

        while start_pointer < end_pointer:
            start_height = height[start_pointer]
            end_height = height[end_pointer]
            if start_height > end_height:  # move the one with a lower height
                # move the pointer but also see if moving to the next one would give a better area
                new_area = get_area(start_pointer, end_pointer - 1)
                if new_area > max_area:
                    max_area = new_area
                end_pointer -= 1
            else:
                new_area = get_area(start_pointer + 1, end_pointer)
                if new_area > max_area:
                    max_area = new_area
                start_pointer += 1
        return max_area
