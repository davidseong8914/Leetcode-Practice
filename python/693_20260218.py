class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binaried = bin(n)


        for i in range(1, len(binaried)):
            if binaried[i] == binaried[i-1]:
                return False

        return True