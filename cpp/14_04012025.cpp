/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()){
            return "";
        }

        if (strs.size() == 1) {
            return strs[0];
        }

        string prefix = strs[0];

        for (string word : strs) {
            int min_val = min(word.length(), prefix.length());
            prefix = prefix.substr(0, min_val);
            for (int i = 0; i < min_val; i++) {
                if (prefix[0] != word[0]) {
                    return "";
                }
                if (prefix[i] != word[i]) {
                    prefix = prefix.substr(0, i);
                    
                }
            }
            
        }
        return prefix;
    }
};