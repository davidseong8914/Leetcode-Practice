class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        fibo = [0] * 38
        fibo[0], fibo[1], fibo[2] = 0, 1, 1
        for j in range (3, len(fibo)):
            fibo[j] = fibo[j-3] + fibo[j-2] + fibo[j-1]
        
        return fibo[n]

        