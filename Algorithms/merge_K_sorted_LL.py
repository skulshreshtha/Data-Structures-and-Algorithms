# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge_two_lists(self, l1, l2):
        cur = ans = ListNode(0)
        
        while (l1 and l2):
            if(l1.val <= l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        while(l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next
            
        while(l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
            
        return ans.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if(len(lists) == 0):
            return None
        
        ans = lists[0]
        
        for i in range(1,len(lists)):
            ans = self.merge_two_lists(ans, lists[i])
        
        return ans