class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "").upper()
        res = []
        
        count = len(s)

        while count > 0:
            res.append(s[max(count - k, 0):count])
            count -= k
        
        return "-".join(reversed(res))
        
