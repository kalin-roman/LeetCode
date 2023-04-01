class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

def showList(l:ListNode):
    cur =  l
    while cur != None:
        print(cur.val)
        cur = cur.next

def count(n:ListNode):
    c = 0
    while n != None:
        c += 1
        n = n.next
    return c

def sum(n:ListNode):
    _s = 0
    while n :
        _s += n.val
        n = n.next
    return _s


def merge_two_list(l1:ListNode ,l2:ListNode):
    p = r = None
    while l1 or l2:
        n = None
        if not l1 and l2 or l1.val > l2.val:
            n = ListNode(l2.val)
            l2 = l2.next
        elif l1:
            n = ListNode(l1.val)
            l1 = l1.next  
        if p:   
            p.next = n
        else:
            r = n
        p = n

    return r


list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))

b = merge_two_list(list1, list2)

print(showList(b))