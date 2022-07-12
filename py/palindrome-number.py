# # https://leetcode.com/problems/palindrome-number/

# # if palindrome, return True
# # if not, return False


def is_palindrome() -> bool:
  x = 1221

  if x < 0:
    return False

  x_list = [int(i) for i in str(x)]
  x_list_length = len(x_list)

  if x_list_length == 1:
    return True

  while x_list_length > 1:
    
    if x_list[0] == x_list[-1]:
      x_list.pop(0)
      x_list.pop(-1)
      x_list_length = len(x_list)
      if x_list_length <= 1:
        return True
    else:
      return False

print(is_palindrome())