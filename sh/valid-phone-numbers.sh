#!/bin/bash

# Ref: https://medium.com/@ChYuan/leetcode-193-valid-phone-numbers-%E5%BF%83%E5%BE%97-easy-ff49c940d484
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt

# sed is a stream editor for filtering and transforming text. 
# -n: suppress automatic printing of pattern space.
#     For example, if you want to print only the lines
#     that match a pattern, you can use the -n option.
# -r: use extended regular expressions in the script.
#     For example, the following command will print
#     the lines that contain a number followed by a
#     space and then a word:
#     sed -r '/[0-9] [a-zA-Z]+/p' text.txt
# / : the pattern to match.
# ^ : match the beginning of a line.
# $ : match the end of a line.
# [0-9]{3} : match 3 digits.
# [0-9]{4} : match 4 digits.
# [0-9]{3}- : match 3 digits followed by a hyphen.
# [0-9]{3}-[0-9]{4} : match 3 digits followed by a hyphen
#     and then 4 digits.
# [0-9]{3}-|\([0-9]{3}\) : match 3 digits followed by a
#     hyphen or match 3 digits enclosed in parentheses.
# [0-9]{3}-|\([0-9]{3}\) [0-9]{3}-[0-9]{4} : match 3 digits
#     followed by a hyphen or match 3 digits enclosed in
#     parentheses followed by a space, then 3 digits, then
#     a hyphen, then 4 digits.
# p : print the matching lines.