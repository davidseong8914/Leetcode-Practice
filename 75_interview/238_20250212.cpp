/* 
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
*/

#include <iostream>
#include <vector>
#include <list>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        std::vector<int> prefix;
        int mult = 1;


        // prefix pass
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                prefix.push_back(1);
            } else {
                prefix.push_back(prefix[i-1] * nums[i-1]);
            }
        }
        
        // suffix
        for (int j = nums.size() -1; j >= 0; j--) {
            prefix[j] = prefix[j] * mult;
            mult = mult * nums[j];
        }

        return prefix;
    }
};