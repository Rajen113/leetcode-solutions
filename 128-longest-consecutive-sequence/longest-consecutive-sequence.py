class Solution(object):
    def longestConsecutive(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set()
    # Populate the set with all elements from arr
        for num in arr:
            my_set.add(num)

        longest = 0

        # For each number, check if it can start a new sequence
        for num in my_set:
            if num - 1 not in my_set:  # indicates a sequence start
                x = num
                count = 1

                # Expand the sequence as far as possible
                while x + 1 in my_set:
                    count += 1
                    x += 1

                # Track the longest run
                longest = max(longest, count)

        return longest