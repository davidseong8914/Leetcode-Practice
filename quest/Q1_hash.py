class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            find = target - nums[i]
            for j in range(i+1, len(nums)):
                yes = nums[j]
                if yes == find:
                    return [i, j]
        
        