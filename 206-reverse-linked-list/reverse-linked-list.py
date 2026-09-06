# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 
        if not curr: 
            return None
        
        nxt = curr.next 

        while nxt is not None:
            curr.next = prev 
            tmp = nxt.next
            nxt.next = curr
            
            prev = curr 
            curr = nxt 
            nxt = tmp
        
        head = curr
        return curr
