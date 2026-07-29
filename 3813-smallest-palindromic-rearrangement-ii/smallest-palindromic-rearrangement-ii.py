from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = Counter(s)

        half = [0] * 26
        middle = ""

        for ch in sorted(freq):
            if freq[ch] % 2:
                middle = ch
            half[ord(ch) - ord('a')] = freq[ch] // 2

        half_len = sum(half)
        CAP = k

        def comb_cap(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > CAP:
                    return CAP + 1
            return res

        def count_perm(cnt):
            rem = sum(cnt)
            res = 1
            for c in cnt:
                if c:
                    res *= comb_cap(rem, c)
                    if res > CAP:
                        return CAP + 1
                    rem -= c
            return res

        if count_perm(half) < k:
            return ""

        first = []

        for _ in range(half_len):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_perm(half)

                if ways >= k:
                    first.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(first)
        return left + middle + left[::-1]