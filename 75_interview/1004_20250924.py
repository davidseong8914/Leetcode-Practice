class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flips = k
        max_len = 0

        for right, v in enumerate(nums):
            if v == 0:
                flips -= 1

            while flips < 0:
                if nums[left] == 0:
                    flips += 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
