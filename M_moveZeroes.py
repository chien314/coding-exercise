# TC:O(n)
# SC:O(1)

class Solution: 
    def moveZeroes(self, nums): 
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0                           # both i and j start wtih 0, swap if num[j]!=0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j],nums[i]=nums[i],nums[j]   # trivial swap: i is either the same position as j or at 0
                i+=1
