import unittest

# https://leetcode.com/problems/merge-two-sorted-lists/description/

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

def merge_two_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ret_ln = None
    temp = None

    if l1.val < l2.val:
        ret_ln = ListNode(l1.val)
        l1 = l1.next
    else:
        ret_ln = ListNode(l2.val)
        l2 = l2.next

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


class TestValidParen(unittest.TestCase):

    def test_is_valid(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        expected = "1,1,2,3,4,4"
        actual = merge_two_lists(l1, l2)

        self.assertEqual(expected, actual.__str__())


if __name__ == "__main__":
    unittest.main()
