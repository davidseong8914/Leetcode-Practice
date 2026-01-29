class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)

            if a == b:
                continue
            else:
                left = max(a,b) - min(a,b)
                heapq.heappush(max_heap, -left)
        
        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0
