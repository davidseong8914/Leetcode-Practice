class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if len(nums) <2:
            return 0

        nums.sort()

        left = 0
        maximos = 0
        
        for right in range(len(nums)):

            if nums[left] * k < nums[right]:
                left += 1
            
            curmos = right - left + 1
            maximos = max(maximos, curmos)

        return len(nums) - maximos

        