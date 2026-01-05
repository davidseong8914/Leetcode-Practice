class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # sort method
        num_sort = sorted(nums)

        ret_dic = {}

        for i, num in enumerate(num_sort):
            if num not in ret_dic:
                ret_dic[num] = i

        ret_list = []

        for i in nums:
            ret_list.append(ret_dic[i])

        return ret_list
