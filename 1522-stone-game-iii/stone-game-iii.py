class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            total = 0
            best = float('-inf')

            for take in range(1, 4):
                if i + take <= n:
                    total += stoneValue[i + take - 1]
                    best = max(best, total - dp[i + take])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"