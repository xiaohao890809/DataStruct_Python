
def shell_sort(myList):
    """希尔排序"""
    n = len(myList)
    gap = n // 2

    while gap > 0:
        # 插入算法，与普通插入算法的区别就是gap步长
        for i in range(gap, n):
            j = i
            while j > 0:
                if myList[j-gap] > myList[j]:
                    myList[j-gap], myList[j] = myList[j], myList[j-gap]
                    j -= gap
                else:
                    break
        gap //= 2


list1 = [1, 23, 56, 43, 7, 34, 24]
print(list1)
shell_sort(list1)
print(list1)