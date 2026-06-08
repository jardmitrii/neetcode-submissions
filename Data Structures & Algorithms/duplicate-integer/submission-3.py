class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = {v: 1 for v in nums}

        return len(nums) != len(uniq)