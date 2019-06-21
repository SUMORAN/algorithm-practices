'''
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
'''
class Solution:
    def judgeCircle1(self, moves: str) -> bool:
        if moves.count("D") == moves.count("U") and moves.count("L") == moves.count("R"):
            return True
        else:
            return False

    # 以上方法每次调用count时都数了一次，实际上相当于遍历了四次
    # 下面的方法，调用python的collections模块中的Counter类，可以只遍历一次，然后将每个对象出现的次数保存在字典中，接下来的时间复杂度就是1了
    '''
    collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型，分别是：

    OrderedDict类：排序字典，是字典的子类。引入自2.7。
    namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
    Counter类：为hashable对象计数，是字典的子类。引入自2.7。
    deque：双向队列。引入自2.4。
    defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。

    Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。
    计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
    '''

    def judgeCircle(self, moves: str) -> bool:
        countdic = collections.Counter(moves)
        return countdic['D'] == countdic['U'] and countdic['L'] == countdic['R']