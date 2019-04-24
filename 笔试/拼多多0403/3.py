# 假设有一堆袜子，数组中每个数表示袜子的颜色
# 假设两只袜子的色差在某个数值以内，我们可以将其认为是一双袜子
# 求随机取出的两只袜子色差可接受的概率

# 输入：
# {31, 18, 19, 1, 25}
# 10
# 输出：
# 0.400000

# 解题思路:
# 这里因为写的急,其实有重复计算,实际只用计算现在的一半就好了
# 假设袜子总数为N, 总的匹配方案为N*(N-1),实际上还要除以2,只是这里没算
# 有效的匹配方案是色差小于阈值的, 临时解法用的穷举
# 注意题目要求的输出保留到小数点后六位 

import sys
import re
def Solution(n, array):
    array = sorted(array)
    L = len(array)
    total = L * (L-1)
    valid = 0
    for i in range(L):
        for j in range(L):
            if i != j:
                if array[i]-array[j]<=n and array[i]-array[j]>=-n:
                    valid +=1
    return valid/total

if __name__=='__main__':
    line = sys.stdin.readline().strip()
    line = line.replace('{',"").replace('}','').replace(',','')
    array = list(map(int, line.split()))
    n = int(sys.stdin.readline().strip())

    print("%.6f"%Solution(n, array))
