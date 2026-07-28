from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        left = []
        middle = ""

        # Build the left half in lexicographical order
        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))

            # Store the middle character (if any)
            if freq[ch] % 2 == 1:
                middle = ch

        left = "".join(left)

        # Left + Middle + Reverse of Left
        return left + middle + left[::-1]