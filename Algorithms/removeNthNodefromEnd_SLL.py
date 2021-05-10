# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = first_p = second_p = ListNode(0, next= head)
        
        # Making second ptr is n+1 nodes ahead of first
        for i in range(1,n+2):
            second_p = second_p.next
        
        # Going till end of list
        while(second_p):
            first_p = first_p.next
            second_p = second_p.next
        
        # Remove the next element to first ptr
        elem = first_p.next
        first_p.next = elem.next
        elem.next = elem.val =  None    # Help GC
        
        return ans.next