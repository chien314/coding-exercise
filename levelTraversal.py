
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
            
        
#         helper(root, 0)
#         return levels    
