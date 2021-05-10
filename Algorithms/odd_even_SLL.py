# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(not head):
            return head
        
        odd = odd_p = head
        even = even_p = head.next
        
        while(odd_p and even_p and odd_p.next and even_p.next):
            odd_p.next = even_p.next
            odd_p = odd_p.next
            even_p.next = odd_p.next
            even_p = even_p.next
        
        odd_p.next = even
        
        return odd