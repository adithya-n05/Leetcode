#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        sformatted = s.lower()
        sout = ""

        for s in sformatted:
            if s.isalnum():
                sout += s
        
        return sout == sout[::-1]

        
# @lc code=end

