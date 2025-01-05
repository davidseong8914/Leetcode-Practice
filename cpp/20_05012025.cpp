/*
20. Valid PArentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
*/

#include <iostream>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> parenthesis;
        int p_num = 0;

        if (s.length() == 0) {
            return true;
        }
        if (s.length() == 1) {
            return false;
        }

        for (char p : s) {
            if (p == '(' || p == '{' || p == '['){
                parenthesis.push(p);
                p_num++;
            } else {
                if (p_num != 0) {
                if (p == ')' && parenthesis.top() != '(') {
                    return false;
                } else if (p == ']' && parenthesis.top() != '[') {
                    return false;
                } else if (p == '}' && parenthesis.top() != '{') {
                    return false;
                } else {
                    parenthesis.pop();
                    p_num--;
                }
                } else {
                    return false;
                }

            } 
        }
        if (p_num == 0) {
            return true;
        } else {
            return false;
        }
        
    }
};

int main() {
    Solution solution;
    std::cout << solution.isValid("([])");
}
