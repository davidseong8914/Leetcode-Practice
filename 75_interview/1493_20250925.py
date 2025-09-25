class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        lef_idx = 0
        sub = 1 
        count = 0
        max_count = 0

        for ri_idx in range(len(nums)):
            if nums[ri_idx] == 0 and sub > 0:
                sub =- 1
                count+=1 

            elif nums[ri_idx] == 1:
                count += 1
            
            else:
                while sub < 1:
                    if nums[lef_idx] == 0:
                        lef_idx += 1
                        count-=1
                    else:
                        sub += 1

        return max(count - 1, 0)


        