
# s1 = '123' 
# s2 = '456'
# TC:O(m*n)
# SC:O(m+n)

def mulStrings(s1, s2):
    
    s1 = s1[::-1]
    s2 = s2[::-1]
    res = [0]*(len(s1)+len(s2))
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            
            res[i+j] +=int(s1[i])*int(s2[j])
            res[i+j+1] += res[i+j] // 10  # carry
            res[i+j] = res[i+j] % 10
            
    res = res[::-1]        # [1,2,3]
    
    while res[beg] == 0:
        beg+=1
    res = map(str, res[beg:])  # ['1','2','3']
    return ''.join(res) # ['123']
