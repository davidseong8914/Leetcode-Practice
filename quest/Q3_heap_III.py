import heapq

class Solution:
    def isPossible(self, target):
        pq = []
        total = 0

        for x in target:
            heapq.heappush(pq, -x)
            total += x

        while True:
            mx = -heapq.heappop(pq)
            rest = total - mx

            if mx == 1:
                return True
            if rest == 1:
                return True

            if rest == 0 or mx <= rest:
                return False

            prev = mx % rest
            if prev == 0:
                return False

            heapq.heappush(pq, -prev)
            total = rest + prev