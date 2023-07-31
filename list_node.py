""" 链接表结点类和一个使用结点的简单函数 """


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


def length(head):
    p, n = head, 0
    while p:
        n += 1
        p = p.next
    return n
#length(head)
