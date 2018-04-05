# https://leetcode.com/problems/merge-two-sorted-lists/description/
# [1,2,4]
# [1,3,4]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        temp = self
        l = []
        while(temp != None):
            l.append(str(temp.val))
            temp = temp.next
        
        return ",".join(l)

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ret_ln = None
    temp = None

    if l1.val < l2.val:
        ret_ln = ListNode(l1.val)
    else:
        ret_ln = ListNode(l2.val)

    temp = ret_ln

    while(l1 != None or l2 != None):

        if l1 == None or l2 == None:
            
            if l1 == None:
                temp.next = ListNode(l2.val)
                l2 = l2.next                
            else:
                temp.next = ListNode(l1.val)
                l1 = l1.next
        else:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
        
        temp = temp.next

    return ret_ln

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# print(l1)
print(mergeTwoLists(l1, l2))