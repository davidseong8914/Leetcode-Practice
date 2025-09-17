class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        i = 0

        if len(nums) <= k:
            return (sum(nums) / len(nums))

        max_avg = sum(nums[0:k])/k

        while i <= len(nums)- k:
            new_num = nums[i:i+k]
            if sum(new_num)/k > max_avg:
                max_avg = sum(new_num)/k
            
            i += 1

        return max_avg
        