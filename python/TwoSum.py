class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in sum_dict:
                return [i, sum_dict[diff]]
                
            sum_dict[num] = i 
        
        return []