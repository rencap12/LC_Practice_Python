class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
''' Problem 1
def symmetricHelper(left,right):
  # Both left and right are none, return True
  if not left and not right:
    return True
  # One of the sides is none, which is not symmetrical
  if not left or right:
    return False
  return (left.val == right.val) and symmetricHelper(left.left, right.right) and symmetricHelper(left.right, right.left)
def is_symmetric(root):
  if not root:
    return True

  return is_symmetric(root.left) and is_symmetric(root.right)
'''
tree = TreeNode(1)
left = TreeNode(2)
right = TreeNode(2)
left.left = TreeNode(3)
right.right = TreeNode(3)
left.right = TreeNode(4)
right.left = TreeNode(4)

tree.left = left
tree.right = right
'''
print(is_symmetric(tree))
'''

''' Problem 2
def treePathHelper(root, lst, str):
  if not root: 
    return

  #if not root.left and not root.right:
  str += f'{root.val}'
  treePathHelper(root.left, lst, str)
  lst.append(str)
  treePathHelper(root.right, lst, str)
  return lst


def binary_tree_paths(root):
  lst = []
  if not root:
    return lst
  elif not root.left and not root.right:
    lst.append(root.val)
    return lst
  else:
    str = ""
    return treePathHelper(root, lst, str)

print(binary_tree_paths(tree))
'''
'''
1) Initialize an empty list to store all the paths.
2) Define a helper function `dfs(node, path, paths)` to perform DFS.
    a) If the current node is None, return.
    b) Append the current node's value to the path.
    c) If the current node is a leaf, add the current path to the list of paths.
    d) Otherwise, recursively call the helper function for the left and right children.
3) Call the helper function starting from the root node.
4) Return the list of paths.
'''
def dfs(node, path, paths):
  if not node:
      return

  if path:
      path += "->" + str(node.val)
  else:
      path = str(node.val)

  if not node.left and not node.right:
      paths.append(path)
  else:
      dfs(node.left, path, paths)
      dfs(node.right, path, paths)

def binary_tree_paths(root):
  paths = []
  dfs(root, "", paths)
  return paths

example_tree_1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
example_tree_2 = TreeNode(1)

'''print(binary_tree_paths(example_tree_1))  
print(binary_tree_paths(example_tree_2))  '''

# 3 WORKS LETS GO??? almost
def minHelper(root,prevVal, lowest):
  if not root:
    return lowest
  currentVal = root.val
  # Check if the current nodes' difference is lowest than the lowest and update it
  # print(prevVal, "-", currentVal)
  if abs(prevVal - currentVal) < lowest:
    lowest =  abs(prevVal - currentVal)
    
  prevVal = currentVal
  return min(minHelper(root.left,prevVal,lowest),minHelper(root.right,prevVal,lowest))

def min_diff_in_bst(root):
  if not root:
    return 0
  lowest = float('inf')
  return minHelper(root, 0, lowest)



example_tree_1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
tree2 = TreeNode(1)
tree2.left = TreeNode(0)
right = TreeNode(48)
tree2.right = right
right.left = TreeNode(12)
right.right = TreeNode(49)

tree3 = TreeNode(15)
tree3.right = TreeNode(1000)
tree3.left = TreeNode(99)
print("example tree:",min_diff_in_bst(example_tree_1))
print("tree2:",min_diff_in_bst(tree2))
print("tree3:",min_diff_in_bst(tree3))
# it was really nice working with you!
# connecting would be awesome! : https://www.linkedin.com/in/renecacapuno/
# Thnx same here, bet, sent
#awesome, gn!

#This is the answer!! thank you!
'''
def min_diff_in_bst(root):
  def in_order_traversal(node, values):
      if not node:
          return
      in_order_traversal(node.left, values)
      values.append(node.val)
      in_order_traversal(node.right, values)

  values = []
  in_order_traversal(root, values)

  min_diff = float('inf')
  for i in range(1, len(values)):
      min_diff = min(min_diff, values[i] - values[i - 1])

  return min_diff

# Example Input Tree #1:
#     4
#    / \
#   2   6
#  / \  
# 1   3
#
# Input: root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
# Expected Output: 1
#
# Example Input Tree #2:
#    1
#   / \
#  0  48
#     / \  
#    12 49
#
# Input: root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
# Expected Output: 1

example_tree_1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
example_tree_2 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))

print(min_diff_in_bst(example_tree_1))  
print(min_diff_in_bst(example_tree_2))  

print(min_diff_in_bst(tree3))


lowest on the left side = 0

lowest = 0
currentVal = 1
prevVal = 1
2- 1 > 0

        4
      /   \
    2       6
  /   \    
1      3 



'''
