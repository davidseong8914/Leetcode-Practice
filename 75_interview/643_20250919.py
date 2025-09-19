class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = sum(nums[:k])
        i = k

        while i < len(nums):
            current_sum = current_sum + nums[i] - nums[i-k]
            if current_sum > max_sum:
                max_sum = current_sum
            
            i += 1

    
        return max_sum/k            