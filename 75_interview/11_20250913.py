class Solution(object):
    def maxArea(self, height):
        # min height * index diff
        max_area = 0

        for i in range(len(height)):
            j = len(height)-1
            while j > i:
                if (j-i) * min(height[i], height[j]) > max_area:
                    max_area = (j-i) * min(height[i], height[j])
                j-=1
        
        return max_area

