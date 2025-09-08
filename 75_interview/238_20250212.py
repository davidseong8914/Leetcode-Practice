# 238. Product of Array Except Self

import numpy as np 

class Solution(object):
    def productExceptSelf(self, nums):        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = []
        mult = 1


        # suffix pass
        for i in range(len(nums)):
            if i == 0:
                answer.append(1)
            else:
                answer.append(answer[i-1] * nums[i-1])
        
        # answer = [1, 1, 2, 6]

        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * mult
            mult = mult * nums[i]

        return answer
    

