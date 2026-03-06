class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        one_seg = s.split("0")
        filtered = list(filter(None, one_seg))

        # or 
        # result = [x for x in text.split("0") if x]
        
        if len(filtered) > 1:
            return False
        else:
            return True
        