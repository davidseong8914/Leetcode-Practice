/*
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
*/
#include <iostream>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        std::string merged;
        int i = 0;

        while (i < std::min(word1.size(), word2.size())) {
            merged.push_back(word1[i]);
            merged.push_back(word2[i]);
            i++;
        }

        if (word1.size() > word2.size()) {
            merged += word1.substr(i);
        } else {
            merged += word2.substr(i);
        }

        return merged;
        
    }
};