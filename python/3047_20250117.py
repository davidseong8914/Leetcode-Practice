# class Solution(object):
#     def largestSquareArea(self, bottomLeft, topRight):
#         """
#         :type bottomLeft: List[List[int]]
#         :type topRight: List[List[int]]
#         :rtype: int
#         """
#         max_area = 0

        # for i in range(len(bottomLeft)):
        #     for j in range(i+1, len(bottomLeft)):
        #         if bottomLeft[j][0] < topRight[i][0] and bottomLeft[j][1] < topRight[i][1]:     # < 1st square's max y
        #             max_area = min(topRight[i][0]-bottomLeft[j][0], topRight[i][1]-bottomLeft[j][1])

        # return max_area**2

class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        max_side = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                # Find the boundaries of the intersection rectangle
                # The bottom-left of the intersection is the max of the bottom-lefts
                inter_bl_x = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_bl_y = max(bottomLeft[i][1], bottomLeft[j][1])
                
                # The top-right of the intersection is the min of the top-rights
                inter_tr_x = min(topRight[i][0], topRight[j][0])
                inter_tr_y = min(topRight[i][1], topRight[j][1])

                # Calculate width and height of the intersection
                width = inter_tr_x - inter_bl_x
                height = inter_tr_y - inter_bl_y

                # If width and height are positive, an intersection exists
                if width > 0 and height > 0:
                    # The largest square in this rectangle has side = min(width, height)
                    side = min(width, height)
                    max_side = max(max_side, side)

        return max_side * max_side



