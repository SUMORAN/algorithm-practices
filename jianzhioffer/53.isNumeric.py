# -*- coding:utf-8 -*-
"""表示数值的字符串
    题目描述
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
    
    解题：
    因为12e会匹配成12，只要匹配成功就会返回true。加上^ 和 $是让整个字符串必须和正则表达式匹配的意思，这样12虽然和前面的正则表达式匹配成功，但是e不成功，所有返回False
"""
class Solution:
    # s字符串
    def isNumeric(self, s):
        if not s:
            return False
        import re
        if re.match(r'^[\+\-]?[\d]*(\.\d*)?([eE][\+\-]?[\d]+)?$', s):
            return True
        else:
            return False