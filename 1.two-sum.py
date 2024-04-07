#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index in range(len(nums)):
            if target - nums[index] in nums[index+1:]:
                return [nums[index+1:].index(target-nums[index]) + index+1, index]
        
        return []

        
# @lc code=end

