class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(d) for d in str(n)]
        digits.sort(reverse=True)
        return digits[0] * digits[1]