# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = set()
        node = head
        while node: 
            if node in l:
                return True
            l.add(node)
            node = node.next
        return False
        