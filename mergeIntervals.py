# [Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.

#  intervals = [[1,3],[2,6],[8,10],[15,18]]
  
  class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort(key=lambda x: x[0])
      
      prev_s, prev_e = intervals[0]
      res = []
      for i in range(1, len(intervals)):
        curr_s, curr_e = intervals[i]
        if prev_e > curr_s:
          intervals[i] = prev_s, max(prev_e, curr_e)
          res.append()
          
