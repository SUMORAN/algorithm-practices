# -*- coding:utf-8 -*-
import sys
"""
判断一个字符串是否是双对称字符串
双对称字符串定义如下：
（1）字符串是一个对称字符串（顺序和逆序一样），如aabbaa
（2）字符串长度是偶数，如aabaa就不符合要求
（3）字符串中第一个字符和第二个字符一致，第三个字符和第四个字符一致，以此类推
如：aabbccbbaa
同时满足以上三个条件的字符串成为双对称字符串

输入描述：
多行（可能一行，可能多行）长度小于1k的字符串

输出描述：
对于每一行输出一行，即假设输入有3行字符串，那么输出也有3行
"""
def shuangduichen(string):
    string = string.strip()
    print(len(string))
    if not string:
        print("长度为0")
        return False
    if len(string)&1:
        print("长度为奇数")
        return False
    reverse = string[::-1]
    if reverse == string:
        i = 0
        j = 2
        L = len(string)
        double = [] # 每两个拆一组
        while j < L+1:
            double.append(string[i:j])
            i += 2
            j += 2
        new_str = []
        print(double)
        for item in double:
            if len(set(item)) == 1:
                print("00000000000000000000")
                new_str.append(item[0])
            else:
                print("1111111111111")
                return False
        return ''.join(new_str)
    else:
        print(reverse)
        print("不对称")
        return False

for line in sys.stdin:
    res = shuangduichen(line)
    print(res)


