/*
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

*/

#include <iostream>
#include <map>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {

        std::map<int, int> origin;    
        std::vector<int> return_vector;    

            for (int num: nums) {
                // if found
                if (origin.find(num) != origin.end()) {
                    origin[num]++;
                } // if not found
                else {
                    origin[num] = 1;
                }

            }

            for (auto number : origin) {
                return_vector.push_back(number.first);
            }

            nums = return_vector;

            return return_vector.size();

        
            }
};