class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] == 2:
                res.append(-1)
            else:
                t = nums[i] + 1
                lowbit = t & -t  
                res.append(nums[i] - (lowbit >> 1))

        return res

        