class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0
        for i, f in enumerate(freq):
            pushes = i // 8 + 1
            ans += f * pushes

        return ans
        