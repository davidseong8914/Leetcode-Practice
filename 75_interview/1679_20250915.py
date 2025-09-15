# not optimal but solved in one go
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        used_idx = []
        count = 0

        for idx, num_i in enumerate(nums):
            for idx_j, num_j in enumerate(nums):
                if idx_j >idx:
                    if num_i + num_j == k and idx not in used_idx and idx_j not in used_idx:
                        count += 1
                        used_idx.append(idx)
                        used_idx.append(idx_j)
                        continue
        return count