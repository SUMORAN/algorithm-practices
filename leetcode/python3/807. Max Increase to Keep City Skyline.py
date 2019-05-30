'''
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
'''

'''
分析：实际上就是要求矩阵数字可以增加，但最大不能超过所在行的最大和所在列的最大
'''

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 另外构建一个矩阵，用来存储当前位置所在行和所在列不能超过的最大值，其实这个矩阵就是最终的矩阵了
        # 行最大值
        max_row = []
        for row in grid:
            max_row.append(max(row))
        
        # 列最大值
        grid_column = [[r[col] for r in grid] for col in range(len(grid[0]))]
        max_column = []
        for column in grid_column:
            max_column.append(max(column))

        # grid1 = []
        # for line in grid:
        #     tmp = [0] * len(line)
        #     grid1.append(tmp)
        # print(grid1)
        
        resSum = 0
        for index, i in enumerate(grid):
            for idx, j in enumerate(i):
                # grid1[index][idx] = min(max_row[index], max_column[idx])
                resSum += min(max_row[index], max_column[idx])-j

        # print(grid1)
        return resSum


grid = [ [3, 0, 8, 4], 
         [2, 4, 5, 7],
         [9, 2, 6, 3],
         [0, 3, 1, 0] ]
res = Solution().maxIncreaseKeepingSkyline(grid)
