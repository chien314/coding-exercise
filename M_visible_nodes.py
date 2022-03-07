# TC:O(num of nodes)
# SC:O(height of tree)

import math
# Add any extra import statements you may need here
 

class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

# Add any helper functions you may need here


def visible_nodes(root):
  # Write your code here
    def helper(root, level):
      # base case
      if root is None:
        return level
    
      L = helper(root.left, level+1)
      R = helper(root.right, level+1)
      
      return max(L,R)
    
    return helper(root, 0)
