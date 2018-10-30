import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pro = 0
        l3 = ListNode(0)
        tmp = l3
        while l1 or l2 or pro:
            v = pro
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            pro = v / 10
            v = v % 10
            tmp.next = ListNode(v)
            tmp = tmp.next

        return l3.next