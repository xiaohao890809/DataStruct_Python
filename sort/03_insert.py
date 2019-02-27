
def insert_sort(myList):
    """插入排序法"""
    n = len(myList)
    for i in range(n):
        j = i
        while j > 0:
            if myList[j-1] > myList[j]:
                myList[j-1], myList[j] = myList[j], myList[j-1]
                j -= 1
            else:
                break


list1 = [1, 23, 56, 43, 7, 34, 24]
print(list1)
insert_sort(list1)
print(list1)