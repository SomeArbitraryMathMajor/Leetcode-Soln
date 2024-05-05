# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = []
        t2 = []
        while l1:
            t1.append(l1.val)
            l1 = l1.next
        while l2:
            t2.append(l2.val)
            l2 = l2.next
        val = int(''.join(map(str, t1[::-1]))) + int(''.join(map(str, t2[::-1])))
        valLst = list(map(int, str(val)))[::-1]
        l3 = dummy = ListNode()
        for i in valLst:
            l3.next = ListNode(i)
            l3 = l3.next
        return dummy.next
