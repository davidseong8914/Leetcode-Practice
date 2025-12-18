class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        con = 0
        for i in nums:
            if i == 1:
                con += 1
                if con > max_con:
                    max_con = con
            else:
                con = 0
        
        return max_con
        