class Solution(object):
    def isTrionic(self, nums):
        if len(nums) < 4:
            return False    

        stage = 0
        moved = False 

        for i in range(1, len(nums)):
            if stage == 0:
                if nums[i] > nums[i-1]:
                    moved = True
                elif nums[i] < nums[i-1] and moved:
                    stage = 1

                else:
                    return False

            elif stage == 1:
                if nums[i] < nums[i-1]:
                    pass
                elif nums[i] > nums[i-1] and moved:
                    stage = 2
                else:
                    return False

            elif stage == 2:
                if nums[i] > nums[i-1]:
                    pass
                else:
                    return False

        return stage == 2 and moved