class Solution:
    def longestBalanced(self, s: str) -> int:
        res_max = 0
        tot_len = len(s)

        for i in range(tot_len):
            freq = {}
            max_freq = 0

            for j in range(i, tot_len):
                sublen = j - i + 1
                freq[s[j]] = freq.get(s[j], 0) + 1
                max_freq = max(max_freq, freq[s[j]])
                if len(freq) * max_freq == sublen:
                    res_max = max(sublen, res_max)

        return res_max




        