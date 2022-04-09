# s = "ADOBECODEBANC", t = "ABC", return "BANC"
# TC:O(max(m,n)), where m=len(s) and n=len(t)
# SC:O(max(m,n))
from collections import Counter
def MWS(s,t): 
    lent, dic = len(t), Counter(t)
    I=J=i=0
    for j,c in enumerate(s,1):
        lent -= dic[c] > 0    # if dic[c]>0: lent-=1 
                dic[c]-=1
           
        if lent == 0:
            while dic[s[i]]<0:  # i<j?
                dic[s[i]]+=1
                i+=1
            if J==0 or J-I > j-i:
                I,J =i,j 
    return s[I:J]  
        
 
