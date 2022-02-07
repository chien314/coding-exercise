# Method 1. Recursion
# TC:O(n)
# SC:O(n)
# start with this one-node example
class Solution:
    def levelOrder(self, root):
        levels=[]
        
        def helper(node, level):
            if not node:
                return 
 
            levels.append([])
                
            levels[level].append(node.val)            
        
        helper(root, 0)
        return levels
        
# full solution        
class Solution:
    def levelOrder(self, root):
        levels=[]
        
        def helper(node, level):
            if not node:
                return 
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            helper(node.left, level+1)
            helper(node.right, level+1)
                   
        helper(root, 0)
        return levels    

#     Method 2, iteration: using queue
from collections import deque
class Solution:
    def levelOrder(self, root):
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels        
