class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """

        n = len(s)
        tree = [None] * (4 * n)

        # Node:
        # [left_char, right_char, left_len, right_len, max_len, size]

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            left_len = a[2]
            right_len = b[3]

            max_len = max(a[4], b[4])

            # If the boundary characters are same,
            # we can combine the two runs.
            if a[1] == b[0]:
                max_len = max(max_len, a[3] + b[2])

                # Entire left segment has same character
                if a[2] == a[5]:
                    left_len = a[5] + b[2]

                # Entire right segment has same character
                if b[3] == b[5]:
                    right_len = a[3] + b[5]

            return [
                left_char,
                right_char,
                left_len,
                right_len,
                max_len,
                a[5] + b[5]
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],   # left_char
                    s[l],   # right_char
                    1,      # left_len
                    1,      # right_len
                    1,      # max_len
                    1       # size
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build initial segment tree
        build(1, 0, n - 1)

        ans = []

        # Process queries
        for i in range(len(queryCharacters)):
            idx = queryIndices[i]
            char = queryCharacters[i]

            update(1, 0, n - 1, idx, char)

            # Root contains answer for complete string
            ans.append(tree[1][4])

        return ans