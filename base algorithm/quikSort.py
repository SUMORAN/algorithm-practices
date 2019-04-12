# 一行
quikSort = lambda array: array if len(array) <= 1 else quikSort([item for item in array[1:] if item <= array[0]]) + quikSort([item for item in array[1:] if item > array[0]])

def quikSort(array, l, r):
    """
        array如果是个列表的话，可以通过len(array)求得长度，
        但是后边递归调用的时候必须使用分片，而分片执行的原列表的复制操作，
        这样就达不到原地排序的目的了，所以还是要传上边界和下边界的。
    """
    if l > r:
        return
    low = l
    high = r
    key = array[low] # 左侧的数字做哨兵
    while l > r:
        while l < r and array[r] > key:
            r -= 1
        array[l] = array[r] # 把现在指向的数字换到假设为空的位置去
        #一侧交换出校了换位置之后就去操作另一侧
        while l < r and array[l] <= key:
            l += 1
        array[r] = array[l] # 把现在指向的数字换到假设为空的位置去
    array[r] = key
    quikSort(array, low, l-1)
    quikSort(array, l+1, high)
    