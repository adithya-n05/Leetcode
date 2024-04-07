#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsorted = sorted(nums)

        maxlen = 0
        currentcount = 0

        if len(nums) == 0:
            return maxlen

        for index in range(len(numsorted)-1):
            if numsorted[index+1] == numsorted[index] + 1:
                currentcount += 1
            elif numsorted[index+1] == numsorted[index]:
                continue
            else:
                maxlen = max(currentcount, maxlen)
                currentcount = 0
        
        maxlen = max(currentcount, maxlen)

        return maxlen + 1
        
# @lc code=end

