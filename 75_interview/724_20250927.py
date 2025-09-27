class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_idx = 0
        left_sum = 0
        right_sum = sum(nums[1:])
        
        if left_sum == right_sum:
            return left_idx

        for i in range(1, len(nums)):
            left_sum = left_sum + nums[i - 1]
            right_sum = right_sum - nums[i]

            if left_sum == right_sum:
                return i
        
        return -1



