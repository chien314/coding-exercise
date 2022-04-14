# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            L= dfs(root.left)
            R= dfs(root.right)

            diameter= max(diameter, L+R)
            return max(L,R)+1
        
        diameter=0

        dfs(root)
        return diameter

# case 2
#1522
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(root):
            nonlocal diameter
            maxd1 = maxd2 = 0
            for child in root.children:
                d = dfs(child)
                if d > maxd1:
                    maxd2, maxd1 = maxd1, d
                elif d > maxd2:
                    maxd2 = d
            diameter = max(diameter, maxd1+maxd2)
            return maxd1 + 1
        
        diameter = 0
        dfs(root)
        return diameter
    
# case 3
#1245
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def dfs(root, parent):
            nonlocal diameter
            maxd1 = maxd2 = 0 # 2 max depth branches
            for child in graph[root]:
                if child != parent: # only one way traversal is allowed, dont go back to parent
                    d = dfs(child, root)
                    if d > maxd1:
                        maxd2, maxd1 = maxd1, d
                    elif d > maxd2:
                        maxd2 = d
            diameter = max(diameter, maxd1+maxd2)
            return maxd1+1
        
        if not edges:
            return 0
        
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        diameter = 0
        dfs(0, -1)
        return diameter
    
# case 4
#124
class Solution:
    def maxPathSum(self, root: TreeNode) -> int
        def dfs(root):
            nonlocal maxsum
            if not root:
                return 0
            ls, rs = dfs(root.left), dfs(root.right)
            maxsum = max(maxsum, root.val+max(0,ls)+max(0,rs))
            return root.val + max(0, ls, rs)
            
        maxsum = float('-inf')
        dfs(root)
        return maxsum
    
