# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = dummy = ListNode()
        if not list1 and not list2:
            return dummy.next
        elif not list1:
            return list2
        elif not list2:
            return list1
        while list1 or list2:
            if not list1:
                val, cur = list2.val, False
            elif not list2:
                val, cur = list1.val, True
            else:
                (val, cur) = (list1.val, True) if list1.val <= list2.val else (list2.val, False)
            list3.next = ListNode(val)
            list3 = list3.next
            if cur:
                list1 = list1.next
            else:
                list2 = list2.next
        return dummy.next
