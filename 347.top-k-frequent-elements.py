#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        vals = []

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        while (k > 0):
            maxcount = 0
            maxval = nums[0]
            for num in count:
                if count[num] > maxcount:
                    maxcount = count[num]
                    maxval = num
            vals += [maxval]
            count[maxval] = 0
            k -= 1
        
        return vals

        
# @lc code=end

