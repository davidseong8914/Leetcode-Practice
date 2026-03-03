class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S1 is just "0"
        if n == 1:
            return "0"
        
        # Calculate length of the current string Sn
        length = (1 << n) - 1  # This is 2^n - 1
        mid = length // 2 + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            # If k is in the first half, look at the previous string
            return self.findKthBit(n - 1, k)
        else:
            # If k is in the second half, find the corresponding bit in the first half
            # and invert it.
            # The corresponding index is: length - k + 1
            original_bit = self.findKthBit(n - 1, length - k + 1)
            return "1" if original_bit == "0" else "0"