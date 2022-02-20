# TC:O(x^2) # find max val in a queue of size x for x iteration
# SC:O(n) # create a queue of tuples (n,i)

import math
from collections import deque 

def findPositions(arr, x):
  # Write your code here
  q = deque([(n,i+1) for i,n in enumerate(arr)])
  ret = []
  
  for _ in range(x):
    mx = float('-inf')
    popped = []
    
    j = 0
    while q and j < x:
      n,i = q.popleft()
      if n > mx:
        mx = n
        mxj = j
        mxi = i
      popped.append((max(0, n-1), i))
      j += 1
      
      
    if popped:
      popped.pop(mxj)
    if popped:
      q.extend(popped)
    
    ret.append(mxi)
    
  return ret 
