class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = ""
        for i in str(bin(n)[2:]):
            if i == "1":
                res += "0"
            else:
                res += "1"

        return int(res,2)