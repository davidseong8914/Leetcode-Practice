class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return list(s).sort() == list(goal).sort()

        # if same
        if s == goal:
            return True
        # needs to be shifted
        else:
            for i in range(1, len(s)):
                if s[i:] + s[:i] == goal:
                    return True

        return False




        