class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[None] * n for _ in range(n)]

        def solve(l, r):
            if l == r:
                return nums[l]

            if dp[l][r] is not None:
                return dp[l][r]

            left = nums[l] - solve(l + 1, r)
            right = nums[r] - solve(l, r - 1)

            dp[l][r] = max(left, right)
            return dp[l][r]

        return solve(0, n - 1) >= 0