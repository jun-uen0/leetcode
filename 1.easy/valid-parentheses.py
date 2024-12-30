#   /

# class Solution:
#   def isValid(self, s: str) -> bool:

#     print(s) # "()[]{}"
#     print(type(s)) # <class 'str'>

#     # 1. Convert string to list
#     # 2. Zero and Even numbers of index is the open brackets of the parentheses
#     # 3. Next numbers (odd) of index is the close brackets of the parentheses
#     # 4. If the open brackets and close brackets are not the same, return False
#     # 5. If the open brackets and close brackets are the same, return
#     # 6. If the open brackets and close brackets are the same for all parenthese, return True

#     # convert s to list
#     s_list = list(s)
#     print(type(s)) # <class 'list'>
#     print(s_list) # ['(', ')', '[', ']', '{', '}']
#     print(len(s_list)) # 6

#     # Separate open and close brackets in the s_list
#     # Zero and even number of index will be in open_brackets
#     # Odd numbers of index will be close_brackets
#     open_brackets = []
#     close_brackets = []
#     for i in range(len(s_list)):
#       if i % 2 == 0:
#         open_brackets.append(s_list[i])
#       else:
#         close_brackets.append(s_list[i])

#     print(open_brackets)
#     print(close_brackets)


#     for i in range(len(open_brackets)):
#       if not self.is_same_bracket(open_brackets[i], close_brackets[i]):
#         return False

#     return True
  
#   def is_same_bracket(self, open, close):
#     if open == '(':
#       if close == ')':
#         return True
#       else:
#         return False
#     elif open == '[':
#       if close == ']':
#         return True
#       else:
#         return False
#     elif open == '{':
#       if close == '}':
#         return True
#       else:
#         return False


###############################################################################

# class Solution:
#   def isValid(self, s: str) -> bool:
  
#     stack = [] 
#     lookup = {'(':')','{':'}','[':']'}
  
#     for p in s:
#       if p in lookup.values(): # if p is a close bracket
#         stack.append(p) # add p to stack
#       # if p is a close bracket and the last element in the stack is the open bracket of the same type
#       elif stack and lookup[p] == stack[-1]:
#         stack.pop() # remove the last element in the stack
#       else:
#         return False
  
#     return stack == [] # if stack is empty, return True
    

###############################################################################

class Solution:
  def isValid(self, s: str) -> bool:
    pair = dict(('()', '[]', '{}')) # create a dictionary with key:value pairs
    print(pair) # {'(': ')', '[': ']', '{': '}'}
    st = [] # create an empty stack
    for x in s:
      if x in '([{': # if x is an open bracket
        st.append(x) # if x is an open bracket, add x to the stack
      # if x is a close bracket and the last element in the stack is not the same type of open bracket, return False
      elif len(st) == 0 or x != pair[st.pop()]:
        return False
    return len(st) == 0 # if stack is empty, return True