class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_num = 0
        current_alt = 0

        for num in gain:
            current_alt = current_alt + num
            if current_alt > max_num:
                max_num = current_alt

        
        return max_num
            

