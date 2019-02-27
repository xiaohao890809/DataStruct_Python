
class Node(object):

    def __init__(self, ele):
        self.ele = ele
        self.next = None


class SingleLinkList(object):

    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.ele, end=' ')
            cur = cur.next
        print(' ')

    def add(self, ele):
        """在链表头部添加元素，头插法"""
        node = Node(ele)
        node.next = self.__head
        self.__head = node

    def append(self, ele):
        """在链表尾部添加元素，尾插法"""
        node = Node(ele)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
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
        pre = None
        cur = self.__head
        while cur is not None:
            if cur.ele == ele:
                # 先判断此节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, ele):
        """判断节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.ele == ele:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':


    sig = SingleLinkList()
    print(sig.is_empty())
    print(sig.length())

    sig.append(1)
    print(sig.is_empty())
    print(sig.length())
    sig.append(2)
    sig.append(3)
    sig.insert(-9, 8)
    sig.travel()
    sig.append(4)
    sig.insert(2, 100)
    sig.travel()
    sig.insert(10, 200)
    sig.travel()
    print(sig.search(2800))
    sig.remove(8)
    sig.travel()
    sig.remove(3)
    sig.travel()
    sig.remove(200)
    sig.travel()
