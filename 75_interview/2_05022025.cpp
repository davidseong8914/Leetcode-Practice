/*
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
*/

#include <iostream>


class Solution {
public:
    std::string divider(std::string max, std::string min) {
        std::string denom;
        while ()
    }

    std::string gcdOfStrings(std::string str1, std::string str2) {

        std::string merged;

        // first letter or last letter isn't the same
        if (str1[str1.size()-1] != str2[str2.size()-1] || str1[0] != str2[0]) {
            return "";
        }

        // if same character
        for (int i =0; i < std::min(str1.size(), str2.size()); i++) {
            if (str1[i] == str2[i]) {
                merged.push_back(str1[i]);
            }
        }

        std::string min;
        std::string max;

        if (str1.size() > str2.size()) {
            min = str2;
            max = str1;
        } else{
            min = str1;
            max = str2;
        }

        // check if max is multiple of min
        if (max.size() % min.size() != 0) {
            // max is multiple of m/2
            merged = min.substr(min.size()/2);
        } else {

        }
        // have to figure out how to stop 
        // merged has to be less than or equal to min string
        // when merged 

        // even number than break down to the smallest

    }
};