class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        pre = 0
        curr = 1

        for i in range(2, n + 1):
            pre, curr = curr, pre + curr

        return curr

        