class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ret = []

        for i in range(1, target[-1] + 1):
            if i in target:
                ret.append("Push")
            else:
                ret.append("Push")
                ret.append("Pop")
        
        return ret