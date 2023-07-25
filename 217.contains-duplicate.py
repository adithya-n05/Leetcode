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

        setOfNum = set()
        
        for i in nums:
            if i in setOfNum:
                print("Found it")
                return True
            setOfNum.add(i)
        return False
        
# @lc code=end

