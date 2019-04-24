# -*- coding:utf-8 -*-
"""
加密解密
解密过程：
数字变英文
按照”小王加密算法”改变源字符串字符排列顺序，同时会改变一些字母的大小写

"""
import sys

for line in sys.stdin:
    line = line.strip().lower()
    line = list(line)
    chars = ['z', 'e', 'r', 'o', 'n', 't', 'w', 'h', 'f', 'u',  'i', 'v', 's', 'x', 'g']
    dic = dict.fromkeys(chars, 0)
    num = {}
    for i in line:
        dic[i] += 1
    if dic['z'] is not 0: # 0
        times = dic['z']
        dic['e'] -= times
        dic['r'] -= times
        dic['o'] -= times
        num['0'] = times
    if dic['w'] is not 0: # 2
        times = dic['w']
        dic['t'] -= times
        dic['o'] -= times
        num['2'] = times
    if dic['u'] is not 0: # 4
        times = dic['u']
        dic['f'] -= times
        dic['o'] -= times
        dic['r'] -= times
        num['4'] = times
    if dic['x'] is not 0:   # 6
        times = dic['x']
        dic['s'] -= times
        dic['i'] -= times
        num['6'] = times
    if dic['g'] is not 0: # 8
        times = dic['g']
        dic['e'] -= times
        dic['i'] -= times
        dic['h'] -= times
        dic['t'] -= times
        num['8'] = times
    if dic['r'] is not 0: # 3
        times = dic['r']
        dic['t'] -= times
        dic['h'] -= times
        dic['e'] -= times*2
        num['3'] = times
    if dic['f'] is not 0: # 5
        times = dic['f']
        dic['i'] -= times
        dic['v'] -= times
        dic['e'] -= times
        num['5'] = times    
    if dic['s'] is not 0: # 7
        times = dic['s']
        dic['e'] -= times*2
        dic['v'] -= times
        dic['n'] -= times
        num['7'] = times
    if dic['o'] is not 0: # 1
        times = dic['o']
        dic['n'] -= times
        dic['e'] -= times
        num['1'] = times 
    if dic['i'] is not 0: # 9
        times = dic['i']
        dic['n'] -= times*2
        dic['e'] -= times
        num['9'] = times
    
    result = [] 
    for k in num.keys():
        for j in range(num[k]):
            result.append(k)
    print(result)
    result = sorted(result)
    print(result)
    if result:
        result = ''.join(result) 
        print(result)
    else:
        print("None")


