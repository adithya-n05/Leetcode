#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while i >= 0:
            if count > 0 and s[i]  == " ":
                return count
            elif s[i] == " " and count == 0:
                i-= 1
            else:
                count += 1
                i -= 1
        return count
# @lc code=end
            

