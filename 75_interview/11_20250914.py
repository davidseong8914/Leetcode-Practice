# solved # used two pointer hint - initially I thought using two pointer wouldn't check every combination and there would be an outlier that can only be detected by 2 for loops. While this method doesn't go through all possible combinations, it efficiently checks by continuously keeping the best area variable while moving the two pointers.
# could be optimzed by skipping voer bars that are shorter

class Solution(object):
    def maxArea(self, height):
        # min height * index diff
        max_area = 0
        # area = 0

        i = 0
        j = len(height)-1

        while j > i:
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            
            if height[i] > height[j]:
                j -= 1
            else:
                i+= 1
                
        
        return max_area

