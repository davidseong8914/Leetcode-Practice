from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        s = []
        count = 1
        s.append(chars[0])  # seed with first char

        # walk from second char to end
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                # close previous group
                if count > 1:
                    s.append(str(count))
                # start new group
                s.append(chars[i])
                count = 1

        # flush the last group
        if count > 1:
            s.append(str(count))

        # write back in place
        chars[:len(s)] = s
        return len(s)
