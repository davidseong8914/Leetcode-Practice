class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # count = len(cost)
        # cost_accum = 0

        # while count > 1:
        #     count = (count - 1) if (cost[count-1] < cost[count-2]) else count-2
        #     cost_accum += cost[count]
        #     print(count)

        count = -1
        cost_accum = 0

        while count < len(cost) - 2:
            count = (count + 1) if cost[count+1] < cost[count+2] else (count + 2)
            cost_accum += cost[count]


        return cost_accum
        