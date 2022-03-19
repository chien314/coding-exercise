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
