/*
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
*/
#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) {
        std::string x_string = std::to_string(x);
        bool palindrome = true;

        for (int i = 0; i < x_string.size(); i++) {
            if (x_string[i] != x_string[x_string.size() - 1 - i]) {
                palindrome = false;
            }
        }

        return palindrome;

        }
        
    };