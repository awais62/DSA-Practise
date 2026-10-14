import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

  def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    min_heap = []

    # Initialize the heap with the first node of each non-empty linked list
    for i, l in enumerate(lists):
      if l:
        # We include index 'i' as a tie-breaker because Python's heapq
        # cannot compare ListNode objects directly if their values are equal.
        heapq.heappush(min_heap, (l.val, i, l))

    while min_heap:
      val, i, node = heapq.heappop(min_heap)
      curr.next = node
      curr = curr.next

      # If there is a next node in the same linked list, push it into the heap
      if node.next:
        heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next