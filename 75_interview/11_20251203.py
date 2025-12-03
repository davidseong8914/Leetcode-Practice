class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        l_idx = 0 
        r_idx = len(height) - 1

        while (l_idx < r_idx):
            width = r_idx - l_idx
            h1 = height[l_idx]
            h2 = height[r_idx]
            area = min(h1, h2) * width

            if (area > maxArea):
                maxArea = area
            
            if (h1 > h2):
                r_idx = r_idx - 1
            else:
                l_idx = l_idx + 1
        return maxArea
        