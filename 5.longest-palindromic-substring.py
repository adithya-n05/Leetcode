#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pal_substring = ""
        
        for index in range(1, len(s)):
            if index < len(s) - 1 and index > 0:
                pointer1 = index - 1
                pointer2 = index + 1
            if s[pointer1] == s[pointer2]:
                while pointer1 > 0 and pointer2 < len(s) - 1:
                    pointer1 -= 1
                    pointer2 += 1
                    if s[pointer1] != s[pointer2]:
                        break
            elif s[index] == s[pointer2]:
                pointer1 = index
                while pointer1 > 0 and pointer2 < len(s) - 1:
                    pointer1 -= 1
                    pointer2 += 1
                    if s[pointer1] != s[pointer2]:
                            break
            elif s[index] == s[pointer1]:
                pointer2 = index
                while pointer1 > 0 and pointer2 < len(s) - 1:
                    pointer1 -= 1
                    pointer2 += 1
                    if s[pointer1] != s[pointer2]:
                            break
            if len(s[pointer1:pointer2]) > len(pal_substring):
                 pal_substring = s[pointer1: pointer2]

        return pal_substring
            
                    

        
# @lc code=end

