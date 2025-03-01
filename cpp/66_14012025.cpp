/*
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
*/

#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        for (int i = digits.size() - 1; i>=0; i--) {

            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            } else if (i == 0 && digits[i] == 9) {
                digits[i] = 0;
                digits.insert(digits.begin(), 1);
                return digits;
            } else {
                digits[i] = 0;
            }


        }
        
        return digits;
    }
};

// strategy: go from last element in the vector 
// if 9 = make 0, add 1 to element before (recursive)
// if first element then push 1

