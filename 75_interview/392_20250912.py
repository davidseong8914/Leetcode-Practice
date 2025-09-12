# solved first try # not optimal
# use a for loop that compares components to s to reduce number of calculations

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_len = len(s)
        t_idx = 0
        s_idx = 0

        while sub_len > 0:
            if t_idx >= len(t):
                return False
            else:
                if t[t_idx] == s[s_idx]:
                    s_idx += 1
                    t_idx += 1
                    sub_len -= 1
                else:
                    t_idx += 1
        
        if sub_len == 0:
            return True
        else:
            return False

        