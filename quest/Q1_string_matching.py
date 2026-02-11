class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        repeat = False
        length = len(s)


        for i in range(1, length//2 + 1):
            if length % i == 0:
                # divisible by i
                subs = s[0:i]
                multiple = length // i
                if subs * multiple  == s:
                    return True
        
        return False

