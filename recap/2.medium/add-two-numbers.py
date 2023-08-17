# https://leetcode.com/problems/add-two-numbers

# Problem:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# My solution:
# 1. Use a stack to reverse the linked list. Storing the value in the stack.
# 2. Add the two numbers (stacks) and return the result.

st1 = [2, 4, 3]
st2 = [5, 6, 4]

st1 = [9,9,9,9,9,9,9]
st2 = [9,9,9,9]

st1 = [0]
st2 = [0]

st1 = [2,4,9]
st2 = [5,6,4,9]

def listToInt(lst):
  s = [str(int) for int in lst]
  a_str = "".join(s)
  return int(a_str)

def intToList(num):
  return [int(x) for x in str(num)]

def makeList(lst1: list, lst2: list) -> list:
  lst1.reverse()
  lst2.reverse()
  int1 = listToInt(lst1)
  int2 = listToInt(lst2)
  add = int1 + int2
  print(add)
  return intToList(add)

output = makeList(st1,st2)
output.reverse()
print(output)

# My entire solution code:
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
# class Solution:
#   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
#     st1 = []
#     st2 = []
#     while l1:
#       st1.append(l1.val)
#       l1 = l1.next
#     while l2:
#       st2.append(l2.val)
#       l2 = l2.next
    
#     def listToInt(lst):
#       s = [str(int) for int in lst]
#       a_str = "".join(s)
#       return int(a_str)

#     def intToList(num):
#       return [int(x) for x in str(num)]

#     def makeList(lst1: list, lst2: list) -> list:
#       lst1.reverse()
#       lst2.reverse()
#       int1 = listToInt(lst1)
#       int2 = listToInt(lst2)
#       add = int1 + int2
#       return intToList(add)
    
#     output = makeList(st1,st2)
#     print(output)
#     output.reverse()
    
#     def lst2link(lst):
#       cur = dummy = ListNode(0)
#       for e in lst:
#           cur.next = ListNode(e)
#           cur = cur.next
#       return dummy.next

#     return lst2link(output)
    
    
##############################################################################################
# Other solutions:
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

# class Solution:
#   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     stack1 = []
#     stack2 = []
#     while l1:
#       stack1.append(l1.val)
#       l1 = l1.next
#     while l2:
#       stack2.append(l2.val)
#       l2 = l2.next
#     carry = 0
#     result = None
#     while stack1 or stack2 or carry:
#       val1 = stack1.pop() if stack1 else 0
#       val2 = stack2.pop() if stack2 else 0
#       val = val1 + val2 + carry
#       carry = val // 10
#       val = val % 10
#       result = ListNode(val, result)
#     return result