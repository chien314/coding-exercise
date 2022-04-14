# case 1: TC:O(n), SC:O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        dic = defaultdict(lambda : 0)
        dic[0]=1
        total = 0
        run_sum=0

        for x in nums:
            run_sum+=x
            # k = run_sum - sum => 
            su = run_sum - k
            if su in dic:
                total+=dic[su]
            
            dic[run_sum] +=1 # 
        return total

    
# case 2: TC:O(n), SC:O(n)    
# maxSubArrayLen    
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # [1,-1,5,-2,3]
        # run_sum = [1,0,5,3,6], k=3
        # 
        dic = defaultdict(lambda: 0)
        dic[0]=-1
        mx =0
        run_sum=0
        
        for i, x in enumerate(nums):
            run_sum+=x
            # run_sum - su = k
            su = run_sum -k
            if su in dic:
                if i-dic[su] > mx:
                    mx = i-dic[su]
            if run_sum not in dic:
                dic[run_sum] = i
        
        return mx     
