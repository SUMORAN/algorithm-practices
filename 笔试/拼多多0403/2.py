# 现有数字0-9，已知0-9中每个数字的可用次数
# 另有两个整数A和B，A和B由这些数字组成，并且已知A和B各自的位数
# 两个数可以有一个或多个先导0，求A与B乘积的最小值
# 输入：
# 1 1 1 1 1 1 1 1 1 1
# 1  A的位数
# 9 B的位数
# 输出：
# 0
# 输入：
# 1 3 0 0 0 0 0 0 0 0
# 2
# 2
# 输出：
# 11

# 短的数先尽可能用填充，0用完了再用1，再用2
# 注意边界，如果用0组成短的数够用，结果就直接是0

import sys
import functools
def Solution(times, A_len, B_len):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    A = []
    B = []
    if A_len < B_len:
        if A_len <= times[0]:
            return 0
        for index, item in enumerate(times):
            while time[index]<item and item is not 0:
                if len(A)<A_len:
                    A.append(num[index])
                    time[index] += 1
                elif len(B)<B_len:
                    B.append(num[index])
                    time[index] += 1
    else:
        if B_len <= times[0]:
            return 0
        for index, item in enumerate(times):
            while time[index]<item and item is not 0:
                if len(B)<B_len:
                    B.append(num[index])
                    time[index] += 1
                elif len(A)<A_len:
                    A.append(num[index])
                    time[index] += 1

    A = functools.reduce(lambda x, y:x*10+y, A)
    
    B = functools.reduce(lambda x, y:x*10+y, B)
    return A*B

if __name__=='__main__':

    line = sys.stdin.readline().strip()
    times = list(map(int, line.split()))
    
    A_len = int(sys.stdin.readline().strip())

    B_len = int(sys.stdin.readline().strip())
    

    print(Solution(times, A_len, B_len))
