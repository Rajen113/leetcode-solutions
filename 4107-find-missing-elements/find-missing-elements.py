class Solution(object):
    def findMissingElements(self, nums):
        result = []

        for i in range(min(nums), max(nums) + 1):
            if i not in nums:
                result.append(i)

        return result