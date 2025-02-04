# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1+str2 != str2+str1:
             return ""
        
        i = 0
        denom = []
        merged = ""
        while (i < min(len(str1), len(str2))):
            if (str1[i] == str2[i]):
                denom.append(str1[i])   

            i = i+1
        
        if (len(denom) != 0):
            while (len(str1)%len(denom) or len(str2)%len(denom)):
                    denom = denom[:-1]
        
        
        merged = ''.join(denom)
        return merged