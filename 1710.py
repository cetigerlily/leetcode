class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxes = {}
        for i in range(len(boxTypes)):
            num_box, num_unit = boxTypes[i]
            if num_unit not in boxes:
                boxes[num_unit] = 0
            boxes[num_unit] += num_box

        units = sorted(boxes, reverse=True)
        count = 0
        for i in range(len(units)):
            num_boxes = boxes[units[i]]
            # if can fit all boxes of units[i]
            if truckSize - num_boxes >= 0:
                truckSize -= num_boxes
                count += (num_boxes * units[i])
            else:
                # adding last fraction
                count += (truckSize * units[i])
                return count
        return count
