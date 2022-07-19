# https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4]
# list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
      return list2
    if list2 is None:
      return list1
    if list1.val < list2.val:
      list1.next = self.mergeTwoLists(list1.next, list2) # Recursive call
      return list1
    else: # If list1.val >= list2.val
      list2.next = self.mergeTwoLists(list1, list2.next)
      return list2
  
  # Here is explained the solution:
  # 1. If list1 is None, return list2
  # 2. If list2 is None, return list1
  # 3. If list1.val < list2.val,
  #    list1.next = self.mergeTwoLists(list1.next, list2)
  #    return list1
  # 4. If list1.val >= list2.val,
  #    list2.next = self.mergeTwoLists(list1, list2.next)
  #    return list2
  # 5. Return None if both lists are None