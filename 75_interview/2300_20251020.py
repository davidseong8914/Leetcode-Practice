class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        suc_list = []
        potions.sort()

        for i in spells:            
            l, r = 0, len(potions) - 1
            while l <= r:
                m = (r + l) // 2
                if i * potions[m] >= success:
                    r = m - 1
                else: 
                # i * potions[m] > success:
                    l = m + 1
            suc_list.append(len(potions) - l)
        return suc_list