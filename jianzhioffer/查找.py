# 针对有序查找表，二分查找，时间复杂度O(logn)

def binary_search(lis, key):
    low = 0
    high = len(lis)-1
    time = 0 # 折半次数

    while low <= high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            print("折半次数：",time)
            return mid
    return

if __name__=='__main__':
    lis = [1,2,3,4,5,6,7,8,9]
    res = binary_search(lis, 9)
    print(res)