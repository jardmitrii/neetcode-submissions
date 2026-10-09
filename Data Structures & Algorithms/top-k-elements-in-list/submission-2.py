class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums_freq = Counter(nums)
        most_common = nums_freq.most_common(k)
               
        return list(x[0] for x in most_common)