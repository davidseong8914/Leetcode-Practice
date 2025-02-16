# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_V = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j or j < i:
                    continue

                elif ((j - i) * min(height[i], height[j])) > max_V:
                    max_V = (j - i) * min(height[i], height[j])

        return max_V
        