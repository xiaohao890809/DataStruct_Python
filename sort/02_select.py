
def select_sort(myList):
    """选择排序法"""
    n = len(myList)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if myList[j] < myList[min_index]:
                min_index = j
        myList[i], myList[min_index] = myList[min_index], myList[i]


list1 = [1, 23, 56, 43, 7, 34, 24]
print(list1)
select_sort(list1)
print(list1)