class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        min_num = nums[-1]

        for i in range(k-1, len(nums)):
            min_num = min(nums[i] - nums[i-k+1], min_num)
        return min_num
            
        