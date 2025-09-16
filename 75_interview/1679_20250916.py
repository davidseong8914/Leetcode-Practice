class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        used_idx = []
        count = 0

        for idx, value in enumerate(nums):
            pair = k - value
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] == pair and j not in used_idx and idx < j :
                    used_idx.append(idx)
                    used_idx.append(j)
                    count += 1
                    break
                


        return count