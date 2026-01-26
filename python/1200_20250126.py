class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_diff = float('inf')
        arr.sort()

        res = []

        for i in range(len(arr) - 1):
            if (arr[i+1] - arr[i]) < min_diff:
                res = [[arr[i], arr[i+1]]]
                min_diff = arr[i+1] - arr[i]
            elif (arr[i+1] - arr[i]) == min_diff:
                res.append([arr[i], arr[i+1]])

        return res



        