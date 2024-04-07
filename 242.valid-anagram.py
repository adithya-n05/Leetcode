#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count1 = {}
        count2 = {}

        for c in s:
            if c in count1:
                count1[c] += 1
            else:
                count1[c] = 1
        

        for c in t:
            if c in count2:
                count2[c] += 1
            else:
                count2[c] = 1

        return count1 == count2
        
        
# @lc code=end

