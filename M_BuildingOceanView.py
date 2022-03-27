# TC:O(n)
# SC:O(1)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        mx=heights[-1]
        res=[len(heights)-1]
        for i in reversed(range(len(heights)-1)):
            if heights[i]>mx:
                res.append(i)
                mx=heights[i]
        return res[::-1]
