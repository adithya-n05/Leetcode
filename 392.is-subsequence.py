#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        pointer = 0

        truthchecker = False

        if s == "":
            return True

        for index in range(len(t)):
            if s[pointer] == t[index]:
                pointer += 1
                if pointer == len(s):
                    return True
        return False



        
# @lc code=end

