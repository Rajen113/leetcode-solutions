class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 0

        for i in range(len(word)):
            ans += (i // 8) + 1

        return ans
        