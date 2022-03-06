# similar to subarray sum equals k
# TC:O(n), where n = len(arr)
# SC:O(n)
def numberOfWays(arr, k):
   # Write your code here
    import collections
    hashmap = collections.defaultdict(lambda : 0)
    total = 0
    
    for c in arr:
      # k = sum + c
      sum = k - c
      if sum in hashmap:
        total += hashmap[sum]
      hashmap[c]+=1   
    
    return total
