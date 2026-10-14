# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def swapPairs(self, head: ListNode | None) -> ListNode | None:
    # Dummy node to act as the prev node for the first pair
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
      # Identify the two nodes to swap
      first = prev.next
      second = prev.next.next

      # Perform the swap
      first.next = second.next
      second.next = first
      prev.next = second

      # Move prev two nodes ahead to the start of the next pair
      prev = first

    return dummy.next