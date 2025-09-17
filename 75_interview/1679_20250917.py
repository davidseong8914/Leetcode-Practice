class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums) - 1
        ops = 0
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                ops += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1
        return ops
