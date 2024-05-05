class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in nums and nums.index(diff) > i:
                return [i, nums.index(diff)]
            elif nums.count(diff) > 1:
                return [i, nums.index(diff, i+1)]
