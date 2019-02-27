
class Dequeue(object):
    """双端队列"""

    def __init__(self):
        self.__listt = []

    def add_front(self, item):
        """往队列中添加一个item元素"""
        self.__listt.insert(0, item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        self.__listt.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__listt.pop(0)

    def pop_rear(self):
        """从队列头部删除一个元素"""
        return self.__listt.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__listt == []

    def size(self):
        """返回列队的大小"""
        return len(self.__listt)

if __name__ == '__main__':

    q = Dequeue()
    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    q.add_front(4)
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())