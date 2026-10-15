# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Check if there are at least k nodes remaining
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            
            # 2. Reverse the k nodes
            prev = kth.next
            curr = group_prev.next
            
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # 3. Connect with the rest of the list
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next

    def get_kth(self, curr: ListNode, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr