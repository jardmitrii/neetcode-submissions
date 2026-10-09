class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        for num in nums:
            nums_freq[num] += 1

        heap = []
        for num in nums_freq.keys():
            heapq.heappush(heap, (nums_freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
                       
        return res