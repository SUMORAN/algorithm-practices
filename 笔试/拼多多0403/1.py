# 给定一个长度维偶数的数组arr，将该数组中的数字两两配对并求和，
# 在这些和中选出最大和最小值，请问该如何两两配对，才能让最大值和最小值之差最小
# 输入：
# 4
# 2 6 4 3
# 输出：
# 1

# 排序之后首尾折半相加
# 例如 2 6 4 3
# 排序后 2 3 4 6
# 2+6  3+4

import sys
def Solution(n, array):
    array = sorted(array)
    res = []
    mid = int(n/2)
    for i in range(mid):
        res.append(array[i]+array[-i-1])
    Max = max(res)
    Min = min(res)
    return Max, Min

if __name__=='__main__':
    n = int(sys.stdin.readline().strip())
    
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    
    Max, Min = Solution(n, values)
    print(Max-Min)
