# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        p = 1
        while n >= 10:
            t = n % 10
            p *= t
            s += t
            n//=10       
        if n < 10:
            p *= n
            s += n
        return p-s   