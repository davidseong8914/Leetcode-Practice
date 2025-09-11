# solved in around 30 minutes # first try

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        zero_counter = 0
        skipped = False

        for idx, num in enumerate(nums):
            if num == 0 and skipped == False:
                index = idx
                zero_counter += 1
                skipped = True
            elif num != 0 and skipped == True:
                nums[index] = num
                index += 1
            elif num == 0:
                zero_counter += 1
                
        
        for i in range(zero_counter):
            nums[-1 + -1 * i] = 0



        