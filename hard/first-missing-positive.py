class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L = set(nums)
        for i in range(len(nums)):
            if i+1 not in L: return i+1
        return len(nums)+1
