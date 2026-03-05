class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)
                
        goal_1 = (["0", "1"] * n)[:n]
        goal_2 = (["1", "0"] * n)[:n]

        count_1 = 0
        count_2 = 0

        for i in range(n):
            if s[i] != goal_1[i]:
                count_1 += 1
            if s[i] != goal_2[i]:
                count_2 += 1
        
        return min(count_1, count_2)