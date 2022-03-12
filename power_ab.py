#best solution: T(log_2 N) and S(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        # if n==1:
        #     return x
        if n<0:
            n=-n
            x=1/x
    
        ans=1
        while n > 0:
            if n%2==1:
                ans=ans*x
            x=x*x
            n=n//2  
            
        return ans
      
# T(log_2 N) and S(log_2 N)      
class Solution(object):
  def power(self, a, b):
    """
    input: int a, int b
    return: long
    """ 
    # TC:O(logb)
    # SC:O(logb)
    # write your solution here
    if b==0:
      return 1
    if a==0:
      return 0

    half = self.power(a, b//2)

    return half*half if b%2==0 else half*half*a
