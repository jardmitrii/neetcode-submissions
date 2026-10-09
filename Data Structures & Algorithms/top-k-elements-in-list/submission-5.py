class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        for num in nums:
            nums_freq[num] += 1
        
        sorted_freq = list(key for key in sorted(nums_freq, key=nums_freq.get))
                       
        return sorted_freq[-k:]