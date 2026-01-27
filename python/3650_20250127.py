class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # djikstra - shortest path to goal, visit node once

        # graph with inidividual states
        graph = []
        for i in range(n):
            graph.append([])

        # extract 
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w * 2))

        # djikstra algorith
        # priority queue
        pq = [(0,0)]

        min_cost = {}
        for i in range(n):
            min_cost[i] = float('inf')

        # initialize starting point
        min_cost[0] = 0

        while pq:
            cost, u = heapq.heappop(pq)

            # if goal then return
            if u == n-1:
                return cost

            # if shorter path found
            if cost > min_cost[u]:
                continue
            
            # explore
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        return -1
