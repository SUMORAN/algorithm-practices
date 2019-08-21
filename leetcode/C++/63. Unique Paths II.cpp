/**
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
*/
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        /**
        * 参考62题
        */
        int m;
        m = obstacleGrid.size();
        int n;
        n = obstacleGrid[0].size();
        vector<vector<long>> flag(m, vector<long>(n,0));
        if(obstacleGrid[0][0]==0){
            flag[0][0] = 1;
        }
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){ // 这里的两个循环都从0开始，是因为在第一行和第一列也可能存在障碍，走的通的可能性就为0了
                if(obstacleGrid[i][j]==0){
                    if(j>0 && i>0){
                        flag[i][j] = flag[i-1][j]+flag[i][j-1];
                    }
                    else if(j>0 && i == 0){
                        flag[i][j] = flag[i][j-1];
                    }
                    else if(j==0 && i > 0){
                        flag[i][j] = flag[i-1][j];
                    }
                }
                else{
                    flag[i][j] = 0;
                }
            }
        }
        return flag.back().back();
    }
};