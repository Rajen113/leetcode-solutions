class Solution:
    def uniqueXorTriplets(self, nums):
        dp = [{0}, set(), set(), set()]

        for v in nums:
            for cnt in range(2, -1, -1):
                dp[cnt + 1] |= {x ^ v for x in dp[cnt]}

        # Single-value triplets (x,x,x) and (x,x,y)/(x,y,y)
        return len(dp[3] | set(nums))