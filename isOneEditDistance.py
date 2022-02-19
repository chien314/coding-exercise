TC:O(n)
SC:O(1)

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t)==0:
            return False
        if abs(len(s) - len(t))>=2:
            return False
        
        if len(s) > len(t):
            for i in range(len(t)):
                if s[i] != t[i]:
                    return self.compare(s[i+1:],t[i:])
            return True
        elif len(s) < len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return self.compare(s[i:],t[i+1:])
            return True        
        else:
            for i in range(len(t)):
                if s[i] != t[i]:
                    return self.compare(s[i+1:],t[i+1:])
            return False        
        
        
    def compare(self, si, ti):
        if len(si) != len(ti):
            return False
        for i in range(l
