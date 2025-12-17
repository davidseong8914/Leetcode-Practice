class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        alter_list = []
        count = 0
        while count < len(nums) / 2 :
            alter_list.append(nums[count])
            alter_list.append(nums[count + n])

            count += 1
        
        return alter_list


        