class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find sum of longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Step 2: Find smallest missing integer >= total
        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total
        