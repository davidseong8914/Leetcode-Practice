class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in range(len(nums)):

            idx = (i + nums[i]) % len(nums)
            res.append(nums[idx])

        return res
        