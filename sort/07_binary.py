
"""针对有序序列来说"""
def binary_sort(myList, item):
    """二分查找，递归"""
    n = len(myList)
    if n > 0:
        mid = n // 2
        if item == myList[mid]:
            return True
        elif myList[mid] > item:
            return binary_sort(myList[:mid], item)
        else:
            return binary_sort(myList[mid+1:], item)
    return False

def binary_sort2(myList, item):
    """二分查找，非递归"""
    first = 0
    last = len(myList) - 1
    while first <= last:
        mid = (first + last) // 2
        if myList[mid] == item:
            return True
        elif myList[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


list1 = [1, 2, 34, 43, 47, 56, 77]
print(binary_sort(list1, 47))
print(binary_sort(list1, 67))

print(binary_sort2(list1, 47))
print(binary_sort2(list1, 67))