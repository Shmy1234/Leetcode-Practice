# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        node = head
        while node: 
            l.append(node)
            node = node.next 

        for i in range(len(l)//2):
            a = l[i].next
            l[i].next = l[len(l)-1-i]
            l[len(l)-1-i].next = a
            node = a
        
        if node: 
            node.next = None


        