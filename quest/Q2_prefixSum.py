class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot_sum = sum(nums)

        forward_pass  = 0
        backward_pass = 0

        for i in range(len(nums)):
            if sum(nums[i:]) % p == 0:
                forward_pass = i
                continue

        for j in range(len(nums), -1, -1):
            if sum(nums[:j]) % p == 0:
                backward_pass = j
                continue
        
        return min(forward_pass, backward_pass)




        