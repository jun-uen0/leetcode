# Respect the following format:
# https://leetcode.com/discuss/general-discussion/638847/tree-builder-for-debugging-locally

def tree_builder(s):
  s = s[1:-1].split(',')
  if len(s) == 0:
    return
  nodes = [('root', s[0])]
  for i, c in enumerate(s[1:]):
    if c != 'null':
      if i & 1:
        nodes.append((nodes[i // 2][0] + '.right', c))
      else:
        nodes.append((nodes[i // 2][0] + '.left', c))
  for node in nodes:
    print(node[0] + ' = TreeNode(' + node[1] + ')')

###############################################################################
tree_builder('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)