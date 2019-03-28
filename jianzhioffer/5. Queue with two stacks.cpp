#include <iostream>
#include<stack>
// #include<queue>

/*
* 用两个栈实现队列
* 题目描述: 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
*/

class Solution
{
public:
    void push(int node) {
        stack1.push(node); //入队列直接入
    }

    int pop() {
        // 当栈2不为空时，pop
        // 栈2已经是排好的出队列的顺序
        if(!stack2.empty()){
            int res = stack2.top();
            stack2.pop();
            return res;
        }
        
        else if (stack1.empty()){ //如果栈1为空，则无数据可弹出
            return NULL;
        }
        
        else if (stack1.size()==1){ //栈2为空栈1不为空且只有一个数据
            int res = stack1.top();
            stack1.pop();
            return res;
        } // 栈2为空栈1不为空且不只一个数据
        else{
            while(!stack1.empty()){ // 将栈1中的数据依次转移到栈2中
                stack2.push(stack1.top());
                stack1.pop();
            }
            int res = stack2.top();
            stack2.pop();
            return res;
        }     
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};