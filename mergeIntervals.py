# [Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.

#  intervals = [[1,3],[2,6],[8,10],[15,18]]
  
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key= lambda x:x[0])

        currI=intervals[0]
        res=[currI]        
        # res.append()

        # for nextI in intervals:
        for i in range(1,len(intervals)):
            nextI=intervals[i]
            currS, currE = currI
            nextS, nextE = nextI
            
            if currE>=nextS:
                currI[1]=max(currE,nextE)

            else:
                
                res.append(nextI)
                currI=nextI
        return res
