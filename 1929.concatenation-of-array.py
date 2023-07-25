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
        ans = [0] * 2 * len(nums)
        for j in range(len(nums)):
            ans[j], ans[j+len(nums)]= nums[j], nums[j]
        
        return ans
        
# @lc code=end

