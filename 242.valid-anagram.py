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
        dictOfLetters = {}
        dictOfLettersT = {}

        for i in range(len(s)):
            if s[i] in dictOfLetters:
                dictOfLetters[s[i]] = dictOfLetters[s[i]] + 1
            else:
                dictOfLetters[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in dictOfLetters:
                return False
        
        for i in range(len(t)):
            if t[i] in dictOfLettersT:
                dictOfLettersT[t[i]] = dictOfLettersT[t[i]] + 1
            else:
                dictOfLettersT[t[i]] = 1

        if dictOfLettersT != dictOfLetters:
            return False
        
        return True

# @lc code=end

