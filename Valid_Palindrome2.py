# TC:O(N)
# SC:O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            if s[i] != s[n-1-i]:
                return self.vp(s,i,n-i-2) or self.vp(s,i+1,n-i-1)
             
        return True
    
    def vp(self, s, begin, end):
        i,j = begin, end
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1                
            
        return True
