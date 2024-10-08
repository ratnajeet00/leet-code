# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:

# Input: n = 2
# Output: [1,2]
 

# Constraints:

# 1 <= n <= 5 * 104

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        def dfs(cur, n, res):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                if 10*cur+i > n:
                    return
                dfs(10*cur+i, n, res)
        
        res = []
        for i in range(1, 10):
            dfs(i, n, res)
        return res
    