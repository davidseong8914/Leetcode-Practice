class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            # email
            at_split = s.lower().split("@")
            return at_split[0][0] + "*" * 5 + at_split[0][-1] + "@" +at_split[1]
        else:
            # phone numner
            num = ''.join(c for c in s if c.isdigit())
            base = "***-***-" + num[-4:]
            print(base)
            if len(num) == 10:
                return base
            else:
                #11, 12, 13 digit numbers
                return "+" + "*" * (len(num)%10) + "-" + base