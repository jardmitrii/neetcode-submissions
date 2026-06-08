class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = {}
        for i in nums:
            uniq[i] = 1

        return len(nums) != len(uniq)