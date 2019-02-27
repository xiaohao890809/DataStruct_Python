
def merge_sort(myList):
    """归并排序"""
    n = len(myList)
    if n == 1:
        return myList
    mid = n // 2

    # left采用归并排序后形成有序的新列表
    left_list = merge_sort(myList[:mid])

    # right采用归并排序后形成有序的新列表
    right_list = merge_sort(myList[mid:])

    # 将两个有序的子序列合并为一个新的整体
    left_pointer = 0
    right_pointer = 0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result += left_list[left_pointer:]
    result += right_list[right_pointer:]

    return result


list1 = [1, 23, 56, 43, 7, 34, 24]
print(list1)
sorted_list = merge_sort(list1)
print(sorted_list)