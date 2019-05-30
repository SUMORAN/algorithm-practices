#include <iostream>
#include <string>

class Solution {
    public:
        bool judgeCircle(string moves) {
            if(count(moves.begin(), moves.end(), 'D') != count(moves.begin(), moves.end(), 'U')) {
                return false;
            }
            if(count(moves.begin(), moves.end(), 'L') != count(moves.begin(), moves.end(), 'R')) {
                return false;
            }
            return true;   
        }
} 