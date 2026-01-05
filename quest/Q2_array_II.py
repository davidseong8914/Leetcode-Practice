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

        # list method

        # freq = [0] * 101

        # for num in nums:
        #     freq[num] += 1
        
        # cur_sum = 0

        # smaller = [0] * 101
        # for i in range(len(smaller)):
        #     smaller[i] = cur_sum
        #     cur_sum += freq[i]

        # ret_list = []

        # for i in nums:
        #     ret_list.append(smaller[i])

        # return ret_list

