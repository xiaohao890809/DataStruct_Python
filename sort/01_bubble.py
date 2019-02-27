
def bubble_sort(input_list):
    """冒泡排序"""
    length = len(input_list)
    for j in range(length - 1):
        # 当列表已经是有序列表的，节省空间
        count = 0
        for i in range(length - j - 1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                count += 1
        if count == 0:
            return


list1 = [1, 3, 64, 2, 89, 45, 32, 120, 66]
# list1 = [1, 3, 64, 67]
print(list1)
bubble_sort(list1)
print(list1)