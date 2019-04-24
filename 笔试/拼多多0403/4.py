# 将word1变成word2，输出最少操作数
# 可进行的操作为: 添加一个字母、删除一个字母、替换一个字母
# 输入：
# horse
# ros
# 输出：
# 3

# 输入: 
# intention
# execution
# 输出:
# 5


import sys
def Solution(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    L_2 = len(word2)
    L_1 = len(word1)
    anchor = -1
    same = -1
    for i in range(L_2):
        for j in range(anchor+1, L_1):
            if word1[2]==word1[j]:
                same += 1
                anchor = j
    steps = L_2 - same

    return steps

if __name__=='__main__':
    word1 = sys.stdin.readline().strip()
    
    word2 = sys.stdin.readline().strip()
    res = Solution(word1, word2)
    print(res)
