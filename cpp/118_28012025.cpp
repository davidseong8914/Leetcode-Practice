/*
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
*/

#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> pascal;
        std::vector<int> temp;

        int i = 0;
        while (i < numRows) {
            temp = {};
            if (i == 0) {
                temp = {1};
            } else {
                for (int j = 0; j <= i; j++) {
                    if (j == 0) {
                        temp.push_back(1);
                    } else if (j == i) {
                        temp.push_back(1);
                    } else {
                        int sum = pascal[i-1][j-1] + pascal[i-1][j];
                        temp.push_back(sum);
                    }
                }
            }
            pascal.push_back(temp);
            i++;

        }

        return pascal;
    }
};