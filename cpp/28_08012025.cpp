/*
28. Find the Index of the First Occurence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
*/


#include <iostream>
#include <vector>

class Solution {
public:
    int strStr(std::string haystack, std::string needle) {
        // when needle doesn't fit in haystack
        if (needle.length() > haystack.length()) {
            return -1;
        }

        int start_idx = 0;
        int counter = 0;
        bool compat = false;

        if (haystack == needle) {
            return 0;
        }

        for (int i = 0; i < haystack.size(); i++) {
            if (compat == false) {
                if (counter == needle.size()) {
                    compat = true;
                    break;
                }
                if (haystack[i] == needle[0]) {
                    start_idx = i;
                }

                if (haystack[i] == needle[counter]) {
                    counter++;
                } else {
                    counter = 0;
                }

                std::cout << compat;

            } 
        }

        if (compat == true) {
            return start_idx;
        } else {
            return -1;
        }
        
    }
};


int main() {
    std::string haystack = "leetcode";
    std::string needle = "leeto";

    Solution solution;
    solution.strStr(haystack, needle);

    return 0;
}