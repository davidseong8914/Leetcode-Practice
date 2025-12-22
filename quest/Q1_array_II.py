class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_dict = {}
        
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        cor_num, dup_num = -1, -1

        for x in range(1, len(nums) + 1):
            if num_dict.get(x, 0) == 0:
                cor_num = x
            if num_dict.get(x, 0) > 1:
                dup_num = x

        return [dup_num, cor_num]

