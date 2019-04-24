#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# 求a b的和
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# 给出n阶方阵里的所有数，求方阵里所有数的和
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)