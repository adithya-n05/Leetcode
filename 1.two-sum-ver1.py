#
# @lc app=leetcode id=1 lang=python3
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

        for i in range(len(nums)):
            SearchValue = target - nums[i]
            for j in range(i, len(nums)):
                if j != i:
                    if nums[j] == SearchValue:
                        return i,j

             
        
# @lc code=end

