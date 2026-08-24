# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        elif not l1 and not l2:
            return None
        
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2:
            if l1 and l2:
                carry += l1.val + l2.val
            elif l1:
                carry += l1.val
            elif l2:
                carry += l2.val
                
            if carry < 10:
                curr.next = ListNode(carry)
            else:
                curr.next = ListNode(carry % 10)
            carry = carry // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry != 0:
            curr.next = ListNode(carry)
        
        return dummy.next