/**
 * 数值的整数次方》
 * 题目描述
 * 给定一个double类型的浮点数base和int类型的整数exponent。
 * 求base的exponent次方。
*/

/**
 * 解题思路：
1、考虑边界情况，底数=0时的处理，不要用==，因为在计算机内表示小数时都有误差，
    判断两个值是否相等，只能判断它们之差的绝对值是不是在一个很小的范围内
2、指数为负时的处理，尤其是要记录指数为负且底数为0时，0是没法求倒数的，所以要记录错误
3、相乘时可以考虑指数是奇数还是偶数，用递归的方法，减少乘法运算的次数
4、0的0次方在数学上没有意义，结果可以是1也可以是0，这里要在程序中进行说明
*/

class Solution{
public:
    // 判断两个数是否相等
    bool equal(double num1, double num2) {
        if((num1-num2)>0.00000001 && (num1-num2)<-0.00000001){
            return true;
        }
        else{
            return false;
        }
    }

    double PowerUnsigned(double base, int exponent){
        if(exponent==0.0){
            return 1.0;
        }
        else{
            double result = PowerUnsigned(base, exponent>>1); // 右移运算符代替除以2
            result *= result;
            if(exponent & 0x1 == 1){ //位与运算符代替求余
                result *= base;
            }
            return result;
        }

    }
    double Power(double base, int exponent) {
        if(equal(base, 0.0) && exponent < 0){
            return 0.0;
        }
        else if(equal(base, 0.0) && exponent == 0){
            return 0.0; // 这里0的0次方结果取0
        }
        else if(exponent > 0){
            return PowerUnsigned(base, exponent);
        }
        else{
            return 1.0/PowerUnsigned(base, -exponent);
        }
    }
};