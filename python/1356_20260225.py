from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort() 
        
        bin_dict = {}
        for i in arr:
            bit_count = bin(i).count("1") 

            if bit_count in bin_dict:
                bin_dict[bit_count].append(i)
            else:
                bin_dict[bit_count] = [i]
        
        res_list = []
        for key in sorted(bin_dict.keys()):
            res_list.extend(bin_dict[key])
    
        return res_list