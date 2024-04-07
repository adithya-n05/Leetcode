#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        
        return False
        
# @lc code=end

