/**
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
*/
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // 对于每一个方格d[i][j]来说，到达它的路径条数等于到达d[i-1][j]+d[i][j-1]
        // 对于第一行来说，不存在i-1行
        // 对于后续行来说，计算的其实都是当前行和上一行中内容的和
        // 因此可以用一行来算
        vector<int> a(n, 1); // n列的
        for(int i=1; i<m; i++){
            // cout << i << endl;
            for(int j=1; j<n; j++){
                a[j] += a[j-1];
            }
            // cout << a.back()<<endl;
        }
        return a.back();
    }
};