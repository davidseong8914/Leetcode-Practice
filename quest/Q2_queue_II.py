class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        seconds = 0
        num = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] <= num:
                    seconds += tickets[i]
                else:
                    seconds += num
            else:
                # i > k
                if tickets[i] < num:
                    seconds += tickets[i]
                else:
                    seconds += num - 1

        return seconds



 