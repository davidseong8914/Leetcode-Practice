class Solution:
    def minFlips(self, s: str) -> int:

        n = len(s)

        # attach 2 together to emulate rotation
        s = s + s
    
        alt1 = "01" * n
        alt2 = "10" * n
            
        res = float('inf')     
        diff1, diff2 = 0, 0    
        l = 0                  # left side index
        
        for r in range(len(s)):
            # rotating through all characters
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
                
            # chekcing for window size & adjusting based on it 
            if (r - l + 1) > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
                
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
                
        return res