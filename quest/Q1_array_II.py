class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup_num, cor_num = -1, -1

        n = len(nums)
        counts = {}
        
        for x in nums:
            counts[x] = counts.get(x, 0) + 1 # safe way to get value of x and if none assign 0
            
        # check numbers from 1 to n
        for i in range(1, n + 1):
            count = counts.get(i, 0)
            if count == 2:
                dup_num = i
            elif count == 0:
                cor_num = i
                
        return [dup_num, cor_num]