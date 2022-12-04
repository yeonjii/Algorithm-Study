# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        res_tail = res
        quo = 0

        while l1 or l2 or quo:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            quo, rem = divmod(val1 + val2 + quo, 10)

            res_tail.next = ListNode(rem)
            res_tail = res_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

