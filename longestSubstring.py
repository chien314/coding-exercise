#Longest Substring Without Repeating Characters
class Solution:
    def longestSubstring(self, s: str) -> int:  
        distinct = set()
        
        res=0
        i=0
        j=0
        while j < len(s):         
            if s[j] not in distinct:
                distinct.add(s[j])
                j+=1
                res = max(res, j-i)
            else:
                distinct.remove(s[i])
                i+=1

        return res

#longest substring allowing k duplicates
class Solution:
    def longestSubstringK(self, s: str, k: int) -> int:
        from collections import Counter
        
        hmap = collections.defaultdict(lambda : 0)
        res=0
        i,j = 0,0
        while j< len(s):
            if hmap[s[j]] < k:
                hmap[s[j]]+=1
                j+=1
                res=max(res,j-i)
            else:
                hmap[s[i]]-=1
                i+=1
        return res
