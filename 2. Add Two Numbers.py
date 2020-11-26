# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1 = ''
        str2 = ''
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        int1 = int(str1[::-1])
        int2 = int(str2[::-1])
        result = int1 + int2
        
                
        s = str(result)[::-1]
        head = prev = None
        for ch in s:
            node = ListNode(int(ch))
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev
        return head