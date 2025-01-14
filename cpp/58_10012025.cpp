/* 58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
*/



#include <iostream>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int lastIndex = 0;
        int firstIndex = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            // if s ends with ' '
            if (s[i] != ' ' && lastIndex == 0) {
                lastIndex = i;
            } else if (s[i] == ' ' && firstIndex == 0 && lastIndex != 0) {
                firstIndex = i + 1;
                break;
            } else {
                continue;
            }

        }
        return s.substr(firstIndex, lastIndex - firstIndex + 1).length();
        
    };

// strategy:
// start from the end 1. start with a non ' ' letter, iterate to find index with another ' ' or index 0, then return substring