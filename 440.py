# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

# Example 1:

# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
# Example 2:

# Input: n = 1, k = 1
# Output: 1
 

# Constraints:

# 1 <= k <= n <= 109

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n+1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps

        cur = 1
        k -= 1
        while k > 0:
            steps = count_steps(n, cur, cur+1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
