class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0

        for num in nums:
            xor ^= num

        # Entire array itself is valid
        if xor != 0:
            return len(nums)

        # Total XOR is 0.
        # Remove any one non-zero element.
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # All elements are 0
        return 0