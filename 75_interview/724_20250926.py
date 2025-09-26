class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_idx = 0
        right_idx = len(nums) -1

        left_sum = 0
        right_sum = nums[len(nums) - 1]

        while left_idx < right_idx + 1:
            if left_sum >= right_sum:
                right_idx = right_idx - 1
                right_sum = right_sum + nums[right_idx]
            else:
                left_idx += 1
                left_sum += nums[left_idx - 1]
        
        if left_sum == right_sum:
            return left_idx - 1
        else:
            return -1
        