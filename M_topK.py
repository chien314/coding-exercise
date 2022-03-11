class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res=[]
        d = Counter(nums)
        heap_max=[(-v, k) for k,v in d.items() ]
        heapify(heap_max)
        for i in range(k): # pop k smallest
            res.append(heappop(heap_max)[1])
        return res
