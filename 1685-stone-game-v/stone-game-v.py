class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        
        # Prefix sum array to get interval sums in O(1) time
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        def get_sum(i, j):
            return pref[j + 1] - pref[i]

        # dp[i][j]: Max score obtainable from subarray stoneValue[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j]: Max of (dp[i][k] + sum(i, k)) for all k from i to j
        max_l = [[0] * n for _ in range(n)]
        
        # max_r[i][j]: Max of (dp[k][j] + sum(k, j)) for all k from i to j
        max_r = [[0] * n for _ in range(n)]
        
        # Base case Initialization for single elements
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        # Process the intervals bottom-up
        for i in range(n - 1, -1, -1):
            mid = i
            for j in range(i + 1, n):
                # Shift mid rightward to find the largest index where Left Sum <= Right Sum
                while mid + 1 < j and get_sum(i, mid + 1) <= get_sum(mid + 2, j):
                    mid += 1
                
                res = 0
                # Case 1: Elements from i to mid where Left Sum <= Right Sum
                if get_sum(i, mid) <= get_sum(mid + 1, j):
                    res = max(res, max_l[i][mid])
                    
                    if get_sum(i, mid) == get_sum(mid + 1, j):
                        res = max(res, max_r[mid + 1][j])
                    elif mid + 2 <= j:
                        res = max(res, max_r[mid + 2][j])
                else:
                    # Case 2: Left Sum > Right Sum for the rest of the interval
                    res = max(res, max_r[i + 1][j])
                
                dp[i][j] = res
                
                # Update prefix and suffix helper grids for future intervals
                current_total = get_sum(i, j)
                max_l[i][j] = max(max_l[i][j - 1], dp[i][j] + current_total)
                max_r[i][j] = max(max_r[i + 1][j], dp[i][j] + current_total)
                
        return dp[0][n - 1]
