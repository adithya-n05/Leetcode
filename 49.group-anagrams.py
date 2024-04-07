#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def counter(str1):
            dictval = [0] * 26
            for char in str1:
                dictval[ord(char) - ord("a")] += 1
            return dictval

        
        outputdict = {}

        for index in range(len(strs)):
            if tuple(counter(strs[index])) in outputdict:
                outputdict[tuple(counter(strs[index]))] += [strs[index]]
            else:
                outputdict[tuple(counter(strs[index]))] = [strs[index]]
        
        return outputdict.values()
            
                    
        
        
# 
# @lc code=end

