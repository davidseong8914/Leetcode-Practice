class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # math to figure out how many can be placed (too many edge cases though)
        for i in range(len(flowerbed)):
            if n == 0:
                break
            else:
                pass

            if len(flowerbed) == 1:
                if flowerbed[0] == 0:
                    flowerbed[0] = 1
                    n = n-1
            
            if i == 0: # if first 
                if flowerbed[i] == 0 and flowerbed[i+1] ==0:
                    flowerbed[i] = 1
                    n = n - 1
            elif i == len(flowerbed) - 1: # if last
                if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                    flowerbed[-1] == 1
                    n = n - 1
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] =  1
                n = n - 1
            else:
                pass
        
        if n == 0:
            return True
        else:
            return False

            


