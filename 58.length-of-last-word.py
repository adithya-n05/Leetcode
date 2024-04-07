#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        storeval = 0
        newlen = 0

        for index in range(len(s)):
            if s[index] != " ":
                newlen +=1
            elif s[index] == " " and newlen != 0:
                storeval = newlen
                newlen = 0

        if newlen!= 0:
            storeval = newlen
        
        return storeval



        
# @lc code=end

