
class Node(object):

    def __init__(self, ele):
        self.ele = ele
        self.next = None
        self.prev = None


class DoubleLinkList(object):

    """双链表"""
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
        node.next.prev = node

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
            node.prev = cur

    def insert(self, pos, ele):
        """在链表指定位置添加元素"""
        if pos <= 0:
            self.add(ele)
        elif pos > self.length() - 1:
            self.append(ele)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node = Node(ele)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, ele):
        """删除指定元素"""
        cur = self.__head
        while cur is not None:
            if cur.ele == ele:
                # 先判断此节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        #判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
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


    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())
    dll.append(2)
    dll.append(3)
    dll.insert(-9, 8)
    dll.travel()
    dll.append(4)
    dll.insert(2, 100)
    dll.travel()
    dll.insert(10, 200)
    dll.travel()
    print(dll.search(2800))
    dll.remove(8)
    dll.travel()
    dll.remove(3)
    dll.travel()
    dll.remove(200)
    dll.travel()
