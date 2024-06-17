#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode()
        curr = sum
        carry = 0
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if (carry == 1):
            curr.next =ListNode(1)
        return sum.next
# @lc code=end

