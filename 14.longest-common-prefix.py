#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stringreturn = ""
        count = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    count +=1
                if strs[0][i] != strs[j][i]:
                     return stringreturn
            if count == len(strs)-1:
                    stringreturn = stringreturn + strs[0][i]

# @lc code=end

