#
# @lc app=leetcode id=1299 lang=python
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        maxval = arr[len(arr)-1]

        arr[len(arr)-1] = -1

        for index in range(len(arr)-2, -1, -1):
            temp = arr[index]
            arr[index] = maxval
            maxval = max(temp, maxval)

        return arr
    
        
# @lc code=end

