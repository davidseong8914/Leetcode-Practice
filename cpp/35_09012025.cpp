/*
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/

// notes: binary search tree??
// - how do i do this at O(log n) complexity?

#include <iostream>
#include <vector>

class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() -1;

        while (start <= end) {
            int middle = start + (end - start)/2; // why

            if (nums[middle] == target) {
                return middle;
                // target is smaller than middle
            } else if (nums[middle] > target) {
                end = middle - 1; // why
                // target is larger than middle
            } else {
                start = middle + 1; // why
            }
        }
        return start; // why
    }
};