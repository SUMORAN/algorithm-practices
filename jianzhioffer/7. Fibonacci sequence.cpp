#include <iostream>

/**
* 斐波那契数列
* 题目描述
* 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
* n<=39
**/

// 此题用递归不合理
// 因为递归会产生大量的重复运算，空间复杂度和时间复杂度都会太大

// 可以从小往大计算，并将计算结果保存，避免重复计算,
class Solution {
public:
    int Fibonacci(int n) {
        int result[2] = {0, 1};

        //前两个数及n小于0的
        if(n < 2){
            return result[n];
        }

        int preOne = 1;
        int preTwo = 0;
        int res = 0;
        for(int i=1; i<n; i++){
            res = preOne + preTwo;
            preTwo = preOne;
            preOne = res;
        }
        return res;
    }
};