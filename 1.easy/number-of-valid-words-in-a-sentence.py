class Solution:
  def countValidWords(self, sentence: str) -> int:
    tokens = sentence.split()
    cnt = 0

    for token in tokens:
      if self.containsDigitsCapitals(token):
        print("token is not valid at containsDigitsCapitals: " + token)
        continue
      if self.notValidHyphen(token):
        print("token is not valid at notValidHyphen: " + token)
        continue
      if self.notValidMark(token):
        print("token is not valid at notValidMark: " + token)
        continue
      
      cnt += 1
      
    return cnt

  def containsDigitsCapitals(self, token: str) -> bool:
    for char in token:
      if char.isdigit() or char.isupper():
        return True
    return False

  def notValidHyphen(self, token: str) -> bool:
    if token.count("-") == 0:
      return False
    if token.count("-") > 1:
      return True

    hyphen_index = token.index("-")
    if hyphen_index == 0 or hyphen_index == len(token) - 1:
      return True
    if not token[hyphen_index - 1].isalpha():
      return True
    if not token[hyphen_index + 1].isalpha():
      return True

    return False

  def notValidMark(self, token: str) -> bool:
    marks = ["!", ".", ","]
    marks_cnt = 0
    one_mark = ""

    for mark in marks:
      if token.find(mark) != -1:
        marks_cnt += 1
        one_mark = mark

    if marks_cnt == 0:
      return False
    if marks_cnt > 1:
      return True

    if token.index(one_mark) != len(token) - 1:
      return True
    
    return False

