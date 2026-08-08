class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """

        n = len(word1)
        m = len(word2)

        # last[j] = latest index in word1 from which
        # word2[j:] can be matched greedily from the right.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        ans = []
        j = 0

        # We can use at most one mismatch.
        mismatch_used = False

        for i in range(n):

            if j == m:
                break

            # Case 1:
            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2:
            # Use our one allowed mismatch
            elif not mismatch_used:

                # If this is the last character of word2,
                # no suffix needs to be matched.
                #
                # Otherwise, after choosing i as the mismatch,
                # word2[j+1:] must still be possible.
                if j == m - 1 or i < last[j + 1]:

                    ans.append(i)
                    j += 1
                    mismatch_used = True

        if j == m:
            return ans

        return []