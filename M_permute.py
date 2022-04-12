# TC:O(N * N!) = SC
class Solution:
  def permute(self, nums):
    
    res=[]
    def bt(first):
           
       if first ==len(nums): 
          res.append(nums.copy())

       for i in range(first, len(nums)):
          nums[first], nums[i] = nums[i], nums[first]
          bt(first+1)
          nums[first], nums[i] = nums[i], nums[first]
       return
    bt(0)
    return res
    
            
