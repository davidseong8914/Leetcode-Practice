class Solution:
    def removeStars(self, s: str) -> str:

        s_reform = []
        star_count = 0
        
        for char in reversed(s): 
            if char != '*' and star_count == 0:
                s_reform.append(char)
            elif char == '*':
                star_count += 1
            else:
                star_count -= 1
        
        s_reform = reversed(s_reform)

        return "".join(s_reform)
            

        