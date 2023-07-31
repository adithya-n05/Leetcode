#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i in range(len(nums)):
            Diff = target - nums[i]
            if Diff in prevMap:
                return prevMap[Diff], i
            prevMap[nums[i]] = i

# @lc code=end

