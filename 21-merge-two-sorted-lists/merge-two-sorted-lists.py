# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1 
        n2 = list2

        if not n1 and not n2: 
            return None
        if n1 and not n2:
            return n1 
        if not n1 and n2:
            return n2
        
        if n1.val < n2.val:
            head = n1
            n1 = n1.next
        else: 
            head = n2 
            n2 = n2.next
        
        node = head 
        
        while n1 and n2:
            if n1.val < n2.val:
                node.next = n1
                n1 = n1.next
            else: 
                node.next = n2 
                n2 = n2.next
            
            node = node.next
        
        if n1: 
            node.next = n1
        
        elif n2:
            node.next = n2
        
        return head

