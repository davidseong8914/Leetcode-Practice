/*
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
*/

#include <iostream>
#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        std::vector<int> sorted;

        for (int i = 0; i < m-1;) {
            for (int j = 0; j < n-1;) {
                if (nums2[j] < nums1[i]) {
                    sorted.push_back(nums2[j]);
                    j++;
                } else{
                    sorted.push_back(nums1[i]);
                    i++;
                }
            }
        }

        nums1 = sorted;
    }
};

//// Below for answer (smart use of while loops)

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        std::vector<int> merged;

        int i = 0;
        int j = 0;
    // Merge until one array is exhausted
    while (i < m && j < n) {
        if (nums1[i] <= nums2[j]) {
            merged.push_back(nums1[i]);
            i++;
        } else {
            merged.push_back(nums2[j]);
            j++;
        }
    }
    
    // Add any remaining elements from nums1
    while (i < m) {
        merged.push_back(nums1[i]);
        i++;
    }

    // Add any remaining elements from nums2
    while (j < n) {
        merged.push_back(nums2[j]);
        j++;
    }

        nums1 = merged;
    }
};