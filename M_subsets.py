# TC:O(n*2^n)
# SC:O(n), if including output array O(n+n*2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
