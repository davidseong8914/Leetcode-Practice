class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def max_len(Bars):
            if not Bars: return 1
            Bars.sort()

            streak = 1
            output = 1

            for i in range(1, len(Bars)):
                if Bars[i] == Bars[i-1]+1: # streak
                    streak += 1
                else:
                    streak = 1
                
                output = max(streak, output)
            
            return output + 1
        

        return min(max_len(hBars), max_len(vBars)) ** 2

        