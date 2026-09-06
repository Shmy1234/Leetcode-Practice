# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: 
            return None        
        
        length = 0
        node = head
        while node: 
            length+=1
            node = node.next 
        
        if length == n:
            head = head.next 
            return head
        
        prev = None
        node = head
        count = 0
        
        while node:
            if count == length - n:
                prev.next = node.next 
            
            count +=1
            prev = node 
            node = node.next 
        
        return head