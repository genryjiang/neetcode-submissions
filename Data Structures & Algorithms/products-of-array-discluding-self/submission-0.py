class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        # prefix loop
        for i in range(1, len(nums)):
            # prefix: before
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(len(nums)-2, -1, -1):
            # suffix: after
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res

