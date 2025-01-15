# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max = max(a.size(), b.size())
        num_list = [0]

        for i in reversed(range(max)):
            if i == max:
                return ''.join(num_list)
            
            else:
                try:
                    if a[i] + b[i] == 2:
                        num_list.insert[0, 0]
                    if a[i] + b[i] == 1:
                        num_list.insert[0, 1]
                    else:
                        num_list.insert(0, 0)
                except:
                 pass

        return num_list
    
    

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        
        idxA, idxB = len(a) - 1, len(b) - 1
        
        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1            
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1            

            res.append(str(carry % 2))
            carry = carry // 2
            
        return "".join(res[::-1])
        

