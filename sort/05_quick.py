
def qucik_sort(myList, first, last):
    """快速排序法"""
    if first >= last:
        return
    mid = myList[first]
    low = first
    high = last

    while low < high:
        while low < high and myList[high] >= mid:
            high -= 1
        myList[low] = myList[high]

        while low < high and myList[low] < mid:
            low += 1
        myList[high] = myList[low]

    # 从循环退出时，low==high
    myList[low] = mid

    # 对low左边的列表执行快速排序
    qucik_sort(myList, first, low-1)

    # 对low右边的列表执行快速排序
    qucik_sort(myList, low+1, last)


list1 = [1, 23, 56, 43, 7, 34, 24]
print(list1)
qucik_sort(list1, 0, len(list1)-1)
print(list1)