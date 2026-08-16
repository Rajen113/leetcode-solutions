class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        c0, c1, c2 = cnt

        # If there are no non-zero remainder stones,
        # Alice cannot make the sum divisible by 3 on her move.
        if c1 == 0 and c2 == 0:
            return False

        # Even number of 0-modulo stones
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0

        # Odd number of 0-modulo stones
        return abs(c1 - c2) > 2