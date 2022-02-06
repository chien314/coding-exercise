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