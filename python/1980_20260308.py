class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums) 
        res = "0" * n
        
        while res in nums_set:
            next_val = int(res, 2) + 1
            res = bin(next_val)[2:].zfill(n)
            
        return res

# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         res = []
#         for i in range(len(nums)):
#             if nums[i][i] == '0':
#                 res.append('1')
#             else:
#                 res.append('0')
                
#         return "".join(res)