# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst = lst[::-1]
        tail = dummy = ListNode(lst[0])
        for i in lst[1:]:
            tail.next = ListNode(i)
            tail = tail.next
        return dummy
