# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        res = []
        for i in range(len(lists)):
            while lists[i]:
                res.append(lists[i].val)
                lists[i] = lists[i].next
        res = sorted(res)
        print(res)

        dummy = ListNode(0)
        curr = dummy

        for i in range(len(res)):
            curr.next = ListNode(res[i])
            curr = curr.next

        return dummy.next        