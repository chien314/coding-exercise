TC:O(max(m,n))=SC, with m and n the lengths of the two strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res=''
        carry=0
        i,j = len(num1)-1, len(num2)-1
        while i >=0 or j>=0:
            xi = (ord(num1[i]) - ord('0')) if i>=0 else 0
            xj = (ord(num2[j]) - ord('0')) if j>=0 else 0
           
            val = (xi + xj + carry)%10
            carry = (xi + xj + carry)//10
            res += str(val)
            i-=1
            j-=1
        
        if carry != 0:
            res += str(carry)
        return res[::-1]
            
