# class Solution(object):
#     def maximizeSquareArea(self, m, n, hFences, vFences):
#         """
#         :type m: int
#         :type n: int
#         :type hFences: List[int]
#         :type vFences: List[int]
#         :rtype: int
#         """
#         hFences.extend([1, m])
#         vFences.extend([1, n])
        
#         hFences.sort()
#         vFences.sort()

#         maxArea = -1

#         V_dist = set()
#         for i in range(0, len(vFences)):
#             for j in range(i+1, len(vFences)):
#                 V_dist.add(vFences[j] - vFences[i])

#         for i in range(0, len(hFences)):
#             for j in range(i+1, len(hFences)):
#                 length = hFences[j] - hFences[i]
#                 if length in V_dist:
#                     maxArea = max(length, maxArea)

#         return maxArea**2
            
            

class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        # 1. Include the boundary fences (1 and m/n)
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        # 2. Sort to make distance calculation linear/ordered
        hFences.sort()
        vFences.sort()

        # 3. Store all possible vertical distances in a set for O(1) lookup
        v_distances = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_distances.add(vFences[j] - vFences[i])

        max_side = -1
        
        # 4. Find all possible horizontal distances
        # We check distances from largest to smallest to potentially optimize
        h_distances = []
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_distances.append(hFences[j] - hFences[i])
        
        # Sort horizontal distances descending to find the max square quickly
        h_distances.sort(reverse=True)
        
        for side in h_distances:
            if side in v_distances:
                max_side = side
                break # Found the largest possible side

        # 5. Return area modulo 10^9 + 7 if a square exists
        if max_side == -1:
            return -1
        
        return (max_side * max_side) % (10**9 + 7)
            