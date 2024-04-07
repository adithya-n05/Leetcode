#
# @lc app=leetcode id=1929 lang=python
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        newout = [0] * len(nums) * 2

        for index in range(len(nums)):
            newout[index] = nums[index]
            newout[index + len(nums)] = nums[index]
        
        return newout




        
# @lc code=end

