class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
        res = []

        for i in range(len(prices)):
            discount = 0

            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break

            res.append(prices[i] - discount)
                

        return res

