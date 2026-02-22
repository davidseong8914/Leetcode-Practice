class Solution:
    def binaryGap(self, n: int) -> int:
        # bin_n = format()
        bin_n = bin(n)[2:]

        l_gap = 0
        count = 0

        for i in range(1, len(bin_n)):
            if bin_n[i-1] == "1":
                if bin_n[i] == "1":
                    l_gap = max(1, l_gap)
            
            if bin_n[i] == "0":
                count += 1
            elif bin_n[i] == "1" and count != 0:
                count += 1
                l_gap = max(l_gap, count)
                count = 0
        
        return l_gap
        