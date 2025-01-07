/*
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
*/
#include <iostream>
#include <vector>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        std::vector<int> updated_nums;

        for (int i = nums.size() - 1; i>= 0; i--) {
            if (nums[i] != val) {
                updated_nums.push_back(nums[i]);
            }
        }

        nums = updated_nums;
        return updated_nums.size();
    }
};

// first method - loop through nums and pop val
// second method - create another vector and add if element of nums is not val