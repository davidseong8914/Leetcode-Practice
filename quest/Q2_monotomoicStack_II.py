class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n     = len(temperatures)
        res   = [0] * n
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                    low_day = stack.pop()
                    res[low_day] = i - low_day
            
            stack.append(i)

        return res