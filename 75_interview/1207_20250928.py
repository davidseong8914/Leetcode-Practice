class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = {}
        for num in arr:
            if num not in arr_dict:
                arr_dict[num] = 1
            else:
                arr_dict[num] += 1

        seen = set(arr_dict.values())
        
        if len(seen) != len(arr_dict):
            return False
        else:
            return True

