class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        org_total=(n*(n+1))//2
        return org_total - sum(nums)
        