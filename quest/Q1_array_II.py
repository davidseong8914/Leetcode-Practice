class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        
        dup_num, cor_num = -1, -1
        
        for i in range (1, len(nums)+1):
            if num_dict.get(i, 0) == 0:
                cor_num = i
            if num_dict.get(i) > 1:
                dup_num = i

        return [dup_num, cor_num]

