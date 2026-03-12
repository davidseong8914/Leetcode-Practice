from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = sum(nums[0::2])
        total_odd = sum(nums[1::2])
        
        left_even = 0
        left_odd = 0
        count = 0
        
        for i, num in enumerate(nums):
            # chip away from total
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num
                
            if left_even + total_odd == left_odd + total_even:
                count += 1
                
            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num
                
        return count