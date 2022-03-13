# s = "ADOBECODEBANC", t = "ABC", return "BANC"
# TC:O(max(m,n)), where m=len(s) and n=len(t)
# SC:O(max(m,n))
  
      i,j
def MWS(s,t):
  from collections import Counter
  dic, lent = collections.Counter(t), len(t)
  i = I = J = 0
  for j, c in enumerate(s,1):
      lent -= dic[c] > 0     # dic(t)-dic(s)
      dic[c] -= 1
      if lent==0:
          while i<j and dic[s[i]] < 0: # i<j?
              dic[s[i]] += 1
              i += 1
          if J==0 or j - i <= J - I:
              I, J = i, j
  return s[I:J]     
        
