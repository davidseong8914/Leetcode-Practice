/*
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/

#include <iostream>
#include <map>

#include <iostream>
#include <map>

class Solution {
public:
    int romanToInt(std::string s) {
    std::map<char, int> roman =
    {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

        int num = 0;
        int prev_value = 0;

        for (int i = s.size() - 1; i >= 0; i--) {
            int value = roman[s[i]];
            if (value < prev_value) {
                num -= value;
            } else {
                num += value;
            }
            prev_value = value;
        }
    return num;
    }
};