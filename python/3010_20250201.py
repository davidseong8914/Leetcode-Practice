class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]

        sort_rest = sorted(nums[1:])

        res += sort_rest[0]
        res += sort_rest[1]

        return res

        