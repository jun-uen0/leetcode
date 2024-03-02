# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Problem
# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

## Examples
# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

head = [1,1,1,2,3,3,3]

def deleteDuplicates(head):
  cur = head
  while cur:
    while cur.next and cur.next.val == cur.val:
      cur.next = cur.next.next
    cur = cur.next
  return head