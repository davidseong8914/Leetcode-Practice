class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        odd_count = 0
        even_count = 0

        for i in nums:
            if i % 2 == 0:
                even_count += 1
            else: 
                odd_count += 1

        return 2 * min(odd_count, even_count)