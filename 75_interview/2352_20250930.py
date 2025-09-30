class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # count = 0
        length = len(grid)

        col_dict = {}

        for i in range(length):
            col_list = []
            for j in range(length):
                col_list.append(grid[j][i])

            if tuple(col_list) in col_dict.keys():
                col_dict[tuple(col_list)] += 1
            else:
                col_dict[tuple(col_list)] = 0
        
        for k in grid:
            for key in list(col_dict.keys()):
                if tuple(k) == key:
                    col_dict[tuple(k)] += 1

        return sum(col_dict.values())


            
                
        