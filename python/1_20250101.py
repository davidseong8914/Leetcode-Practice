class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        two_sum = {}
        for i, num in enumerate(nums):
            comp_num = target - num
            if comp_num in two_sum:
                return [two_sum[comp_num], i]
            else:
                two_sum[num] = i



        

            
        