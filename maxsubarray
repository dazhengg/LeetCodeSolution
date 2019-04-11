
class Solution: # Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur = nums[0]
        result_max = nums[0]
        for i in range(1, len(nums)):
            if max_cur + nums[i] > nums[i]:
                max_cur += nums[i]

            else:
                max_cur = nums[i]

            if result_max < max_cur:
                result_max = max_cur

        return result_max
# https://leetcode.com/problems/maximum-subarray/