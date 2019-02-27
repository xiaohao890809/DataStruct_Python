
class Node(object):

    def __init__(self, ele):
        self.ele = ele
        self.next = None


class SingleCycleLinkList(object):

    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历结点
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.ele, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾结点，但尾结点的元素未打印
        print(cur.ele)

    def add(self, ele):
        """在链表头部添加元素，头插法"""
        node = Node(ele)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            # cur.next = self.__head 或者
            self.__head = node
            cur.next = node

    def append(self, ele):
        """在链表尾部添加元素，尾插法"""
        node = Node(ele)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 或者 node.next = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, ele):
        """在链表指定位置添加元素"""
        if pos <= 0:
            self.add(ele)
        elif pos > self.length():
            self.append(ele)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                pre = pre.next
                count += 1
            node = Node(ele)
            node.next = pre.next
            pre.next = node

    def remove(self, ele):
        """删除指定元素"""
        if self.is_empty():
            return

        pre = None
        cur = self.__head
        while cur.next is not self.__head:
            if cur.ele == ele:
                # 先判断此节点是否是头结点
                if cur == self.__head:
                    # 头结点的情况，找尾结点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        # 退出循环，cur指向尾结点
        if cur.ele == ele:
            if cur == self.__head:
                # 链表只有一个结点
                self.__head = None
            else:
                # pre.next = cur.next
                pre.next = self.__head

    def search(self, ele):
        """判断节点是否存在"""
        cur = self.__head
        while cur is not self.__head:
            if cur.ele == ele:
                return True
            cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.ele == ele:
            return True
        return False


if __name__ == '__main__':


    sigCly = SingleCycleLinkList()
    print(sigCly.is_empty())
    print(sigCly.length())

    sigCly.append(1)
    print(sigCly.is_empty())
    print(sigCly.length())
    sigCly.append(2)
    sigCly.append(3)
    sigCly.insert(-9, 8)
    sigCly.travel()
    sigCly.append(4)
    sigCly.insert(2, 100)
    sigCly.travel()
    sigCly.insert(10, 200)
    sigCly.travel()
    print(sigCly.search(2800))
    sigCly.remove(8)
    sigCly.travel()
    sigCly.remove(3)
    sigCly.travel()
    sigCly.remove(200)
    sigCly.travel()
