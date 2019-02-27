
class Queue(object):

    def __init__(self):
        self.__listt = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__listt.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__listt.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__listt == []

    def size(self):
        """返回列队的大小"""
        return len(self.__listt)

if __name__ == '__main__':

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())